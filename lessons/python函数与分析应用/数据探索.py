# -*- coding: utf-8 -*-
# 数据读取

import pandas as pd

df1 = pd.read_csv('out.csv', index_col="日期")
print(df1.head())
print(df1.index.size)

"""
均值：mean
"""

print("均值{:.2f}".format(df1['开盘价'].mean()))
print("中位数{:.2f}".format(df1['开盘价'].median()))

## 众数
from pandas import Series

data = Series([1,2,5,4,5])
print(data.mode())


# 最值
# 所有列的最小值
print(df1.min())
print(df1.max())
print(df1['开盘价'].min())
print(df1['开盘价'].max())

# 极差 最大值-最小值
print(df1['开盘价'].max() - df1['开盘价'].min())

"""
标准差： std
方差： var
"""
print("标准差： {:.2f}".format(df1['开盘价'].std()))
print("方差： {:.2f}".format(df1['开盘价'].var()))

"""
描述性统计分析
"""
statistics = df1.describe()
print(statistics)
print(statistics.loc['mean']) # 获取对应行数据，用列名
print(statistics.iloc[1]) # 获取对应行数据，用下标

# 求极差
print(statistics.loc['max'] - statistics.loc['min'])
list = []

# 添加字段
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
print(statistics)