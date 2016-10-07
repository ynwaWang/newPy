#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import sys
from pandas import DataFrame


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    df = pd.read_csv('ddd160830.csv', encoding="gbk")
    # df[u'经纪人手机号码'] = df[u'经纪人手机号码'].apply(lambda x: str(int(x)))
    for x in df.values:
        x
        print x[0]
