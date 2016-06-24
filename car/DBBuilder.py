#!/usr/bin/python
# -*- coding: UTF-8 -*-


import MySQLdb

TEST_HOST = 'testwinbx.mysql.rds.aliyuncs.com'
TEST_USER = 'winbx_test'
TEST_PASSWD = 'funcitypt001'

ONLINE_HOST = 'insuranceplan.mysql.rds.aliyuncs.com'
ONLINE_USER = 'wy_data'
ONLINE_PASSWD = 'iph4quacheoxooyuiC0Paa9Cho8zi6'


def test_db():
    return DB(TEST_HOST, TEST_USER, TEST_PASSWD, 'baoxian')


def online_db():
    return DB(ONLINE_HOST, ONLINE_USER, ONLINE_PASSWD, 'baoxian')


class DB:
    def __init__(self, host, user, password, selectedDB):
        conn = MySQLdb.connect(
            host=host, user=user, passwd=password, db=selectedDB, charset='utf8', port=3306
        )
        self.conn = conn

    def fetchDict(self, sql):
        cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()

    def fetchOne(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchone()[0]

    def updateOne(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)

    def close(self):
        self.conn.close()
