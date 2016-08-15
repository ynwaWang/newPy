#!/usr/bin/env python
# -*- coding:utf-8 -*-

import PyMysql
from car.cityManager import writeCsv
import json

ONLINE_HOST = 'insuranceplan.mysql.rds.aliyuncs.com'
# ONLINE_USER = 'wy_data'
ONLINE_USER = 'wyhzprod'
# ONLINE_PASSWD = 'iph4quacheoxooyuiC0Paa9Cho8zi6'
ONLINE_PASSWD = 'sVj8JW7Z0hIkVQmvf2Qx'

TEST_HOST = 'testwinbx.mysql.rds.aliyuncs.com'
TEST_USER = 'winbx_test'
TEST_PASSWD = 'funcitypt001'


# mysql = PyMysql.PyMysql()
#
# mysql.newConnection(host=ONLINE_HOST,
#                     user=ONLINE_USER,
#                     passwd=ONLINE_PASSWD,
#                     defaultdb="baoxian")


def update_point(sql, user_id, w_time, product_id, baof, policy_uuid):
    index = policy_uuid[-2:]
    sql = sql % (index, product_id, user_id, w_time)
    updated, cur = mysql.execute(sql)
    # if updated != 1:
    #     print 'fail', user_id, w_time, product_id, baof
    # else:
    #     print 'success', user_id, w_time, product_id, baof
    d = {
        'status': 'success' if updated == 1 else 'fail',
        'user_id': user_id,
        'w_time': w_time,
        'product_id': product_id,
        'baof': baof,
        'policy_uuid': policy_uuid
    }
    return d


fieldKeys = [
    u'status',
    u'user_id',
    u'w_time',
    u'product_id',
    u'baof',
    u'policy_uuid'
]
# fieldnames = [u'状态', u'用户id', u'出单日期', u'产品', u'保费（不准，多了税）', u'uuid']

def writeUseCsv(mysql):
    sqltext = "select t.sales_user_id,(t.writer_time div 1000) as w_time,t.product_id,t.policy_baof,t.policy_uuid as uuid from car_insure_policy_allocation t where t.policy_status = 200 "
    # for test limit 2
    # sqltext += " and sales_user_id = 10606159 limit 2"
    lines, results = mysql.query(sqltext, mode=PyMysql.STORE_RESULT_MODE)
    updatetext = "update sales_user_points_course_%s set course_type = case when reward_value >= 0 then 1 else 2 end,reward_type=7,type_id = %s where user_id=%s and unix_timestamp(create_datetime) = %s"
    # updatetext = "update sales_user_points_course_%s set course_type = case when reward_value >= 0 then 1 else 2 end,reward_type=7,type_id = %s where user_id=%s and reward_value = %s"
    out_r = [update_point(updatetext, row[0], row[1], row[2], int(row[3]), row[4]) for row in results.fetch_row(lines)]

    mysql.closeConnnection()
    writeCsv('fix_user_w_time2.csv', fieldKeys, fieldKeys, out_r)

def matchInsurePremiumGreater2000(mysql,policy_uuid):
    sqltext = "select t.uuid,t.detail_json,t.user_id from sales_insure_policy_%s t where t.uuid = '%s'"
    # policy_uuid = "e3f1cfc02bad4fe1b0374711c30a6a1838"
    index = policy_uuid[-2:]
    sql = sqltext % (index, policy_uuid)
    lines, results = mysql.query(sql, mode=PyMysql.STORE_RESULT_MODE)
    for row in results.fetch_row(lines):
        uuid = row[0]
        detail_json = row[1]
        salesUserId = row[2]
        orderinfo = json.loads(detail_json)
        insurePremium = orderinfo['commercial']['insurePremium'] if (orderinfo.has_key('commercial') and orderinfo['commercial'].has_key('insurePremium')) else 0
        if insurePremium >= 2000:
            print salesUserId, uuid

# 300红包发了2次的记录筛选
def match300BonusHave2Record(mysql):
    for i in range(100):
        index = "%02d" % i
        sqltext = "select t.obj_id,t.user_id from sales_user_account_course_%s t where t.bonus_id = 79 and t.amount = 300 group by t.obj_id HAVING count(0) > 1" % index
        lines, results = mysql.query(sqltext, mode=PyMysql.STORE_RESULT_MODE)
        for row in results.fetch_row(lines):
            sql = "select total_amount,SUM(c.amount),total_amount = SUM(c.amount) from sales_user_account t,sales_user_account_course_%s c where t.user_id = %s and c.user_id = t.user_id" % (index,row[1])
            lines2, results2 = mysql.query(sql, mode=PyMysql.STORE_RESULT_MODE)
            for row2 in results2.fetch_row(lines2):
                print row[0],row[1],row2[0],row2[1],row2[2]

if __name__ == '__main__':
    mysql = PyMysql.PyMysql()
    mysql.newConnection(host=ONLINE_HOST,
                        user=ONLINE_USER,
                        passwd=ONLINE_PASSWD,
                        defaultdb="baoxian")
    # mysql.newConnection(host=TEST_HOST,
    #                     user=TEST_USER,
    #                     passwd=TEST_PASSWD,
    #                     defaultdb="baoxian")
    # sqltext = "select t.policy_uuid,t.sales_user_id,t.policy_baof,t.push_money from car_insure_policy_allocation t,car_insure_recruit_info c where t.writer_time BETWEEN 1469980800000 and 1470118620000 and t.policy_status = 200 and c.certi_status = 3 and t.sales_user_id = c.user_id"

    # lines, results = mysql.query(sqltext, mode=PyMysql.STORE_RESULT_MODE)
    # for row in results.fetch_row(lines):
    #    matchInsurePremiumGreater2000(mysql,row[0])



            # writeCsv('fix_user_baof.csv', fieldKeys, fieldnames, out_r)
            # mysql.com
