# -*- coding: utf-8 -*-
# 序列
import pandas as pd

from pandas import Series

# 创建Series

obj = Series([4, 1, -1, 8])
print(obj)

# index
print(obj.index)

# value
print(obj.values)

# 顺序对应自定义索引
obj2 = Series([4, 1, -1, 8], index=['a', 'c', 'f', "e"])
print(obj2)
print(obj2[obj2 > 0])

# in
print('f' in obj2)

# 通过字典创建Series
dict1 = {"q": 3, "w": 4}
print(dict1)
obj3 = Series(dict1)
print(obj3)

# DataFrame
from pandas import DataFrame

# 创建数据库
# 定义两个列表
position = ["产品经理", "数据分析师", "UI", "开发"]
print(position)

company = ["A", "B", "C"]
df = DataFrame([company, position]).T  # .T 纵向排列
print(df)

# columns 设置列标题
df.columns = ["company", "position"]
print("#####")
print(df)

# 指定index,设置行的标题
df.index = ["A", "3", "C", "D"]  # 需要对应长度
print(df)

# reset_index 索引重置
df = df.reset_index(drop=True)  # 需要赋值
print(df)
df = df.reset_index()
print(df)

# head
print(df.head())

# tail
print(df.tail())
print(df.tail(2))

# 要获取其中某一列的值：方式1
print(df['company'])
# 方式2
print(df.company)

# 获取某一行的值 方式1 loc[index]
print(df.loc[3])

# 方式2
print(df.iloc[2])

# 非数值型的描述
print(df.describe())
