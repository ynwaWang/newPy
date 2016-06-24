#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import csv
import json

import DBBuilder

fieldKeys = [
    u'commercialPremium',
    u'compulsoryPremium',
    u'commercialPushMoney',
    u'compulsoryPushMoney',
    u'commercialRatio',
    u'compulsoryRatio',
    u'push_money',
    u'right',
    u'sumAmount',
    u'total_amount',
    u'mobile',
    u'name',
    u'carNumber',
    u'policy_uuid'
]
fieldnames = [u'商业保费', u'交强保费', u'商业推广费', u'交强推广费', u'商业推广费比例', u'交强推广费比例', u'推广费', u'差距', u'流水汇总', u'账户总额', u'手机',
              u'姓名', u'车牌号',
              u'保单uuid']


def writeCsv(fileName, fieldKeys, fieldNames, out):
    with codecs.open(fileName, 'w+b', 'gbk') as fp:
        writer = csv.writer(fp)

        writer.writerow(fieldNames)

        for row in out:
            writer.writerow([row.get(key) for key in fieldKeys])


def parseOutFromRow(row, conn):
    policy_uuid = row.get('uuid')
    userId = row.get('userId')
    total_amount = row.get('total_amount')
    index = policy_uuid[-2:]

    sql_json = "select detail_json from sales_insure_policy_%s where uuid = '%s'" % (index, policy_uuid)
    detail_json = json.loads(conn.fetchOne(sql=sql_json))

    sql_sum = "select sum(amount) from sales_user_account_course_%s where user_id = %s and obj_id = '%s'" % (index, userId, policy_uuid)
    sumAmount = conn.fetchOne(sql=sql_sum)
    return parse_out(detail_json, sumAmount, total_amount, row)


def parse_out(order, sumAmount, total_amount, info):
    commercial = order.get('commercial').get('insurePremium') if (
        'commercial' in order and 'insurePremium' in order.get('commercial')) else 0.0
    compulsory = order.get('compulsory').get('insurePremium') if (
        'compulsory' in order and 'insurePremium' in order.get('compulsory')) else 0.0

    commercialPushMoney = commercial * 0.5
    compulsoryPushMoney = compulsory * 0.15 if info.get('product_id') == 79 else compulsory * 0.04
    total = round(commercialPushMoney + compulsoryPushMoney, 2)

    d = {
        'commercialPremium': commercial,
        'compulsoryPremium': compulsory,
        'commercialPushMoney': commercialPushMoney,
        'compulsoryPushMoney': compulsoryPushMoney,
        'commercialRatio': 0.5,
        'compulsoryRatio': 0.15 if info.get('product_id') == 79 else 0.04,
        'mobile': info.get('mobile'),
        'name': togbk(info.get('name')),
        'carNumber': togbk(order.get('vehicleInfo').get('licenseNo')),
        'push_money': info.get('push_money'),
        'right': round(info.get('push_money') - total, 2),
        'sumAmount': sumAmount,
        'total_amount': total_amount,
        'policy_uuid': info.get('uuid')
    }
    return d


def togbk(line):
    line = line.encode('gbk', 'ignore')
    line = line.decode('gbk')
    return line


def city_manager():
    conn = DBBuilder.test_db()
    # sql = "select t.product_id,t.policy_uuid as uuid,push_money,u.mobile,u.`name`,u.id as userId,ua.total_amount as total_amount from car_insure_policy_allocation t,car_city_manager ct,sales_user u,sales_user_account ua where t.pay_time BETWEEN 1463500800000 and 1463587200000 and ct.user_id = t.sales_user_id and t.policy_status = 200 and ct.user_id = u.id and ct.user_id = ua.user_id"
    sql = "select t.policy_uuid as uuid,push_money,u.mobile,u.`name`,u.id as userId,ua.total_amount as total_amount from car_insure_policy_allocation t,sales_user u,sales_user_account ua where t.policy_status = 200 and t.car_number in ('浙A688QH','浙AUR176','浙A4JJ00','浙AV006B','皖A53M19','浙A223QB','浙A6LQ51','浙A0GF33','浙A2XD38','浙J4699T','浙AZ791U','浙A772QF') and t.sales_user_id = u.id and t.sales_user_id = ua.user_id order by t.sales_user_id"
    results = conn.fetchDict(sql=sql)
    out_r = [parseOutFromRow(row, conn) for row in results]
    conn.close()

    writeCsv('city.csv', fieldKeys, fieldnames, out_r)


if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

    city_manager()
