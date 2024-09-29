# -*- coding: utf-8 -*-
from pandas import Series
import numpy as np
from pandas import DataFrame

stringSeri = Series(['a', 'b', np.nan, 'e', 'f'])
print(stringSeri)

print(stringSeri.isnull())
print(stringSeri[stringSeri.notnull()])

# drop na 删除空值
stringSeri = stringSeri.dropna()
print(stringSeri)

print("df")
df = DataFrame([
    [1.4, np.nan],
    [7.1, -4.5],
    [np.nan, np.nan],
    [-0.75, 1.4]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(df)

print("df.dropna all")
df = df.dropna(how='all')
print(df.dropna(how='all'))

print("df.dropna any")
df = df.dropna()
print(df)

# fill na
print("df")
df = DataFrame([
    [1.4, np.nan],
    [7.1, -4.5],
    [np.nan, np.nan],
    [-0.75, 1.4]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df = df.fillna(0)
print(df)

print("df fill by column")
df = DataFrame([
    [1.4, np.nan],
    [7.1, -4.5],
    [np.nan, np.nan],
    [-0.75, 1.4]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df = df.fillna({'one': 1, 'two': 2})
print(df)

# 已均值补充缺失值
print("df mean")
df = DataFrame([
    [1.4, np.nan],
    [7.1, -4.5],
    [np.nan, np.nan],
    [-0.75, 1.4]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df = df.fillna(df.mean())
print(df)

