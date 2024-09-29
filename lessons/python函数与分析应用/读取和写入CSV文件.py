# -*- coding: utf-8 -*-

# 读取和写入CSV文件的第一种方法

import pandas as pd
#
# df = pd.read_csv('eastmoney_stock_data.csv')
#
# print(df.head())
#
# # index_col 索引列，在第一列显示, 输出3行
# df = pd.read_csv('eastmoney_stock_data.csv', index_col='开盘价', nrows=3)
# print(df.head())
# print(len(df))
#
# # 第二种读取方式
# df = pd.read_table("eastmoney_stock_data.csv", sep=',')
# print(df.head())
#
# # 如果文件中没有title，可以自己添加title
# mynames = ["日期", "开盘价", "收盘价", "最高价", "最低价", "单数", "金额", "均值", '差率', '净盈利率', '未知']
# df = pd.read_csv('eastmoney_stock_data.csv', header=None, names=mynames)
# print(df)
#
# df.to_csv("out.csv", encoding='utf-8')

# excel 文件读取和写入 直接创建文件会报错
# 第一种
xls_data = pd.read_excel('test_out.xlsx')
print(xls_data.head())

# 第二种
# openyxl

import openpyxl

xls_file = pd.ExcelFile('test.xls')
xls_data = xls_file.parse()
print(xls_data.head())

# 导出到excel
# xlwt,输出xlsx，xls会报错

import xlwt
xls_data.to_excel('test_out.xlsx')