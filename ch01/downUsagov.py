#!/usr/bin/python
# encoding:utf-8

import os
import re
import socket
import time
import urllib
import urllib2
import logging

from bs4 import BeautifulSoup

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

urls = ['http://1usagov.measuredvoice.com/2011/', 'http://1usagov.measuredvoice.com/2012/',
        'http://1usagov.measuredvoice.com/2013/']

path = r"E:\p"

# years = ['2013', '2013', '2012']
years = ['2013']

base_url = 'http://1usagov.measuredvoice.com/'
base_url_pre = 'http://1usagov.measuredvoice.com/bitly_archive/'

regx = re.compile(r".gz\">(.+?)</a>")


def down():
    socket.setdefaulttimeout(30)
    for year in years:
        url = year + ".html"
        # print tim_str() + " print soup start :" + url
        logger.debug(" print soup start :" + url)
        try:
            html = open(url).read()
            # print tim_str() + " print soup ing : " + year
            # logger.debug(" print soup ing : " + year)
            # soup = BeautifulSoup(html)
            # soup = BeautifulSoup(html)
            # print tim_str() + " print soup finish : " + year
            # logger.debug(" print soup finish : " + year)
            # gzs = soup.find_all(href=re.compile("gz"))
            gzs = regx.findall(html)
            for gz in gzs:
                file_name = gz + ".gz"
                gz_url = base_url_pre + file_name
                # print tim_str() + " print download:" + gz_url
                logger.debug(" print download:" + gz_url)
                dest_dir = os.path.join(path, year, file_name)
                try:
                    urllib.urlretrieve(gz_url, dest_dir)
                except Exception, ex:
                    logger.error(ex)
        except Exception, ex:
            logger.error(ex)


def down_gz():
    for url in urls:
        print "print url1 :" + url
        soup = BeautifulSoup(urllib2.urlopen(url), 'html.parser')
        print "print soup finish"
        gzs = soup.find_all(href=re.compile("gz"))
        for gz in gzs:
            gz_url = base_url_pre + gz.string + ".gz"
            print "print download:" + gz_url
            urllib.urlretrieve(gz_url, gz.string + ".gz")
            # with open(gz.string + ".gz", "wb") as code:
            #     print "start :" + gz_url
            #     code.write(f.read())


def down_gz1():
    html = open("index.html").read()
    regx = re.compile(r".gz\">(.+?)</a>")
    result = regx.findall(html)


def schedule(blocknum, bs, size):
    """''
    :param size: 已经下载的数据块
    :param bs: 数据块的大小
    :param blocknum: 远程文件的大小
   """
    per = 100.0 * blocknum * bs / size
    if per > 100 or per == 100:
        per = 100
        print '%.2f%% \t' % per
    else:
        print '%.2f%% \t' % per,


def tim_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == '__main__':
    down()
