#!/usr/bin/env python
# coding=utf-8


import pandas as pd
from pandas import DataFrame
from pandas.util.testing import Series
import sys


def f(x):
    return Series(dict(areas="{%s}" % ', '.join(x['area'])))

def fcity(x):
    return Series(dict(areas="{%s}" % ', '.join(x['city'])))


columns = ['prov', 'city', 'area']

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    df = pd.read_csv('area.csv', encoding="gbk")

    df['provs'] = df["prov_code"].map(str) + ':\'' + df["prov"].map(str) + '\''
    dfProv = DataFrame(df['provs'],columns=['provs']).drop_duplicates()
    dfProv.to_csv('dfProv.csv', encoding='gbk')

    dfCity = DataFrame(df[['prov_code','city','city_code']],columns=['prov_code','city','city_code']).drop_duplicates()
    dfCity['city'] = dfCity["city_code"].map(str) + ':\'' + df["city"].map(str) + '\''
    dfCity = dfCity.groupby(['prov_code']).apply(fcity)
    dfCity.to_csv('dfCity.csv', encoding='gbk')



    df['area'] = df["area_code"].map(str) + ':\'' + df["area"].map(str) + '\''
    dfCiyAndAre = DataFrame(df[['city_code', 'area']], columns=['city_code', 'area'])
    dfCiyAndAre = dfCiyAndAre.groupby(['city_code']).apply(f)
    dfCiyAndAre.to_csv('dfCiyAndAre.csv', encoding='gbk')
