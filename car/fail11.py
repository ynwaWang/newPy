#!/usr/bin/env python
# -*- coding:utf-8 -*-
from car import DBBuilder

STATUS_CODE_INSURE_FAIL = 300
FAIL_MSG = '测试数据'


def fail_one(policy_uuid, conn):
    index = policy_uuid[-2:]
    sql_update = "update sales_insure_policy_%s set status_code=%s,fail_msg='%s' where uuid = '%s'" % (index, STATUS_CODE_INSURE_FAIL, FAIL_MSG, policy_uuid)
    conn.updateOne(sql_update)


if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

    conn = DBBuilder.test_db()
    whereCondition = "where product_id = 76 and policy_status = 50"
    sql = "select policy_uuid from car_insure_policy_allocation " + whereCondition
    results = conn.fetchDict(sql=sql)
    fail_one(results[0].get('policy_uuid'), conn)
    # [fail_one(row.get('policy_uuid'), conn) for row in results]
    sql_update2 = ("update car_insure_policy_allocation set policy_statue=%s,fail_msg='%s'" + whereCondition) % (STATUS_CODE_INSURE_FAIL, FAIL_MSG)
    # conn.updateOne(sql_update2)
    conn.close()
