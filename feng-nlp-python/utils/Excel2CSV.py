#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

import pandas as pd

__author__ = 'Henry'


def pre(text):
    text = str(text).replace('\\', '\\\\').replace('\r', '').replace('\n', '').replace('\t', '').strip()
    if text == 'nan':
        return ''
    else:
        return text


def pre_bool(text):
    if text == '是':
        return '1'
    else:
        return '-1'


# 城市	商户ID	商户名	菜品分类	菜名	是否招牌菜	分量	价格	做法	食材	内容备注	用餐时间	备注	照片编码	照片备注
df = pd.read_excel('~/Downloads/MVP.xlsx', '菜单明细')

print(len(df))
print(df.head())

file = open('/tmp/match3.csv', 'w', encoding='utf-8')
for i in range(len(df)):
    file.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
        pre(df['城市'][i])
        , pre(df['商户ID'][i])
        , pre(df['商户名'][i])
        , pre(df['菜品分类'][i])
        , pre(df['菜名'][i])
        , pre_bool(df['是否招牌菜'][i])
        , pre(df['分量'][i])
        , pre(df['价格'][i])
        , pre(df['做法'][i])
        , pre(df['食材'][i])
        , pre(df['内容备注'][i])
        , pre(df['用餐时间'][i])
        , pre(df['备注'][i])
        , pre(df['照片编码'][i])
        , pre(df['照片备注'][i])
        , 'END'
    ))
file.close()
