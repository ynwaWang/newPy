#!/usr/bin/env python
# -*- coding:utf-8 -*-

import PyMysql
from car.cityManager import writeCsv

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

    sqltext = "select t.sales_user_id,(t.writer_time div 1000) as w_time,t.product_id,t.policy_baof,t.policy_uuid as uuid from car_insure_policy_allocation t where t.policy_status = 200 "
    # for test limit 2
    # sqltext += " and sales_user_id = 10606159 limit 2"
    lines, results = mysql.query(sqltext, mode=PyMysql.STORE_RESULT_MODE)
    updatetext = "update sales_user_points_course_%s set course_type = case when reward_value >= 0 then 1 else 2 end,reward_type=7,type_id = %s where user_id=%s and unix_timestamp(create_datetime) = %s"
    # updatetext = "update sales_user_points_course_%s set course_type = case when reward_value >= 0 then 1 else 2 end,reward_type=7,type_id = %s where user_id=%s and reward_value = %s"
    out_r = [update_point(updatetext, row[0], row[1], row[2], int(row[3]), row[4]) for row in results.fetch_row(lines)]

    mysql.closeConnnection()
    writeCsv('fix_user_w_time2.csv', fieldKeys, fieldKeys, out_r)
    # writeCsv('fix_user_baof.csv', fieldKeys, fieldnames, out_r)
    # mysql.com
