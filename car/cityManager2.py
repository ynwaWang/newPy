#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import csv
import json
from pandas import DataFrame
import data_base

import DBBuilder
fieldKeys = [
    u'company',
    u'carNumber',
    u'policyStatus',
    u'payTime',
    u'successTime',
    u'commercialStart',
    u'commercialNo',
    u'commercial',
    u'compulsoryStart',
    u'compulsoryNo',
    u'compulsory',
    u'travelTax',
    u'sumAmount',
    u'holderName',
    u'holderMobile',
    u'insuredName',
    u'insuredMobile',
    u'salesUserName',
    u'salesUserMobile',
    u'policyUuid'
]

fieldnames = [u'所属公司',
              u'车牌号码',
              u'出单状态',
              u'支付时间',
              u'出单日期',
              u'商业险起保日期',
              u'商业险保单号',
              u'商业险保费',
              u'交强险起保日期',
              u'交强险保单号',
              u'交强险保费',
              u'车船税',
              u'总保费',
              u'投保人姓名',
              u'投保人电话',
              u'被保人姓名',
              u'被保人电话',
              u'保险师',
              u'保险师电话',
              u'保单uuid' ]


def writeCsv(fileName, fieldKeys, fieldNames, out):
    with codecs.open(fileName, 'w+b', 'utf-8') as fp:
        writer = csv.writer(fp)

        writer.writerow(fieldNames)

        for row in out:
            writer.writerow([row.get(key) for key in fieldKeys])


def parseOutFromRow(row, conn):
    policy_uuid = row.get('uuid')
    # userId = row.get('userId')
    index = policy_uuid[-2:]

    sql_json = "select detail_json from sales_insure_policy_%s where uuid = '%s'" % (index, policy_uuid)
    detail_json = json.loads(conn.fetchOne(sql=sql_json))

    return parse_out(detail_json, row)


import time

def timestamp_datetime(value):
    format = '%Y-%m-%d'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value/1000)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

def parse_out(order, info):
    commercialStart=''
    commercialNo=''
    commercial=0
    compulsoryStart=''
    compulsoryNo=''
    compulsory=0
    travelTax=''
    if order.has_key('commercial'):
        commercial = order['commercial']['insurePremium'] if order['commercial'].has_key('insurePremium') else 0
        commercialStart = timestamp_datetime(order['commercial']['validStartDatetime']) if order['commercial'].has_key('validStartDatetime') else ''
        commercialNo = order['commercial']['commercialInsuranceNo'] if order['commercial'].has_key('commercialInsuranceNo') else ''
    if order.has_key('compulsory'):
        compulsory = order['compulsory']['insurePremium'] if order['compulsory'].has_key('insurePremium') else 0
        compulsoryStart = timestamp_datetime(order['compulsory']['validStartDatetime']) if order['compulsory'].has_key('validStartDatetime') else ''
        compulsoryNo = order['compulsory']['compulsoryInsuranceNo'] if order['compulsory'].has_key('compulsoryInsuranceNo') else ''
        travelTax = order['compulsory']['travelTax'] if order['compulsory'].has_key('travelTax') else ''
    sumAmount = commercial + compulsory

    holderName = ''
    holderMobile = ''
    insuredName = ''
    insuredMobile = ''
    if order.has_key('applicantInfo'):
        holderName = order['applicantInfo']['applicantName'] if order['applicantInfo'].has_key('applicantName') else ''
        holderMobile = order['applicantInfo']['applicantMobile'] if order['applicantInfo'].has_key('applicantMobile') else ''
    if order.has_key('insuredInfo'):
        insuredName = order['insuredInfo']['insuredName'] if order['insuredInfo'].has_key('insuredName') else ''
        insuredMobile = order['insuredInfo']['insuredMobile'] if order['insuredInfo'].has_key('insuredMobile') else ''

    d = {
        'company': info.get('company'),
        'carNumber':info.get('carNumber'),
        'payTime':info.get('payTime'),
        'successTime':info.get('successTime'),
        'commercialStart':commercialStart,
        'commercialNo':commercialNo,
        'commercial':commercial,
        'compulsoryStart':compulsoryStart,
        'compulsoryNo':compulsoryNo,
        'compulsory':compulsory,
        'travelTax':travelTax,
        'sumAmount':sumAmount,
        'holderName':holderName,
        'holderMobile':holderMobile,
        'insuredName':insuredName,
        'insuredMobile':insuredMobile,
        'salesUserName':info.get('salesUserName'),
        'salesUserMobile':info.get('salesUserMobile'),
        'policyUuid':info.get('uuid'),
        'policyStatus':info.get('policyStatus')
    }
    return d


def togbk(line):
    # line = line.decode('gbk')
    if(line):
        line = line.encode('utf-8', 'gbk')
    return line


def city_manager():
    conn = DBBuilder.online_db()
    # sql = "select t.product_id,t.policy_uuid as uuid,push_money,u.mobile,u.`name`,u.id as userId,ua.total_amount as total_amount from car_insure_policy_allocation t,car_city_manager ct,sales_user u,sales_user_account ua where t.pay_time BETWEEN 1463500800000 and 1463587200000 and ct.user_id = t.sales_user_id and t.policy_status = 200 and ct.user_id = u.id and ct.user_id = ua.user_id"
    sql = "select t.policy_uuid as uuid,(case t.policy_status when 100 then '已支付' when 200 then '出单' when 500 then '已退款' when 700 then '已退保' when 350 then '核保失败' when 180 then '已付款待出单' else ''  end )as policyStatus, t.policy_status," \
          "t.car_number as carNumber,c.`name` as company,FROM_UNIXTIME(t.pay_time/1000,'%Y-%m-%d') as payTime,FROM_UNIXTIME(t.writer_time/1000,'%Y-%m-%d') as successTime,u.mobile as salesUserName,u.`name` as salesUserMobile,u.id as userId \
from car_insure_policy_allocation t,sales_user u,sales_user_account ua,car_insure_company c where t.sales_user_id = u.id and t.sales_user_id = ua.user_id and t.company_id = c.id \
           and t.pay_time BETWEEN 1469980800000 and 1472659200000 order by t.company_id,t.pay_time desc"
    results = conn.fetchDict(sql=sql)
    out_r = [parseOutFromRow(row, conn) for row in results]
    conn.close()

    writeCsv('all_pay_month8.csv', fieldKeys, fieldnames, out_r)

    # writeCsv('h_uuid.csv', fieldKeys, fieldnames, out_r)

def asdasf():
    return "1212","33333"

class Ax(object) :
    def __init__(self, aaa,xxx):
        self.aaa = aaa
        self.xxx = xxx
    def run(self):
        print self.aaa,self.xxx


if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')
    (aaa,xxx) = asdasf()
    Ax(aaa,xxx).run()


    import yaml,json
    configs = yaml.load(file("spark_pdw_fact_learning.yaml"))

    x = yaml.dump(configs)

    jsonout = json.dumps(configs["job_params"])

    list = [0,1,2,3,4]



    for v in range(1,len(list)) :
        print list[v]


    city_manager()
