# -*- coding: utf-8 -*-
# 创建一个数据框
import numpy as np
from pandas import DataFrame, Series

array = np.arange(16)

data = array.reshape((4, 4))

print(data)

df = DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['1', '2', '3', '4'])
print(df)

# 丢弃指定轴上的项
df = df.drop('b')
print(df)

df = df.drop('2', axis=1)  # axis = 1 表示列
print(df)
# drop 之后就没了
# 查找列4，值为7的记录
df = df[df['1'] == 8]
print("#123123")
print(df)

# 唯一值，unique
obj = Series([1, 2, 3, 3, 4, 2, 6, 5])
print(obj.unique())

# 频率统计 value_counts
print(obj.value_counts())
print(obj.value_counts(sort=False))

