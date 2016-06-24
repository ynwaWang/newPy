#!/usr/bin/python
# encoding:utf-8

import gzip
import logging
import os

SHOW_LOG = True
base_path = r"E:\p"
years = ['2011', '2012', '2013']
BufSize = 1024 * 8

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


def read_txt_write_gz(tpath, gzpath):
    """read the txt-format file with 'rb' and write this file content
    to the gzip-format file"""
    if os.path.exists(tpath):
        if os.path.exists(gzpath):
            if SHOW_LOG:
                print('打开目标文件:[{}]'.format(tpath))
            with open(tpath, 'wb') as t:
                if SHOW_LOG:
                    print('打开gz文件:[{}]'.format(gzpath))
                with gzip.open(gzpath, 'rb') as g:
                    if SHOW_LOG:
                        print('写入内容：[{}]'.format(g))
                    t.writelines(g.read())
                    if SHOW_LOG:
                        print('写入内容完成...')
        else:
            print('the path [{}] is not exist!'.format(gzpath))
    else:
        print('the path [{}] is not exist!'.format(tpath))


def gunZipFile(gzFile, dst):
    fin = gzip.open(gzFile, 'rb')
    fout = open(dst, 'wb')

    in2out(fin, fout)


def in2out(fin, fout):
    while True:
        buf = fin.read(BufSize)
        if len(buf) < 1:
            break
        fout.write(buf)
    fin.close()
    fout.close()


def gz_year(year_i):
    # file_list = []
    org_base_path = os.path.join(base_path, year_i)
    dest_path = des_path(year_i)
    for path in os.listdir(org_base_path):
        # file_list.append(s.decode('gbk'))
        # g = gzip.GzipFile(mode="rb", fileobj=open(os.path.join(org_base_path, path), 'rb'))
        filename = os.path.splitext(path)[0]
        org_file_path = os.path.join(org_base_path, path)
        dest_file_path = os.path.join(dest_path, filename)
        # open(file_path, "wb").write(g.read())
        # read_txt_write_gz(dest_file_path, org_file_path)
        # gunZipFile(org_file_path, dest_file_path)
        g = gzip.GzipFile(mode="rb", fileobj=open(org_file_path, 'rb'))  # python gzip 解压
        try:
            open(dest_file_path, "wb").write(g.read())
            print('写入内容完成...' + dest_file_path)
        except Exception, ex:
            logger.error(ex)


def clear0(year_i):
    dest_path = des_path(year_i)
    [del0file(dest_path,path) for path in os.listdir(dest_path)]


def del0file(dest_path, file_path):
    filename = os.path.join(dest_path, file_path)
    if os.path.getsize(filename=filename) == 0:
        os.remove(filename)


def des_path(year_i):
    return os.path.join(base_path, year_i + "gz")


if __name__ == '__main__':
    [gz_year(year) for year in years]
    [clear0(year) for year in years]
