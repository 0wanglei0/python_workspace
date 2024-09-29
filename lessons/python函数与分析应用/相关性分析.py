# -*- coding: utf-8 -*-
## 相关性分析 数据读取
import pandas as pd

df2 = pd.read_csv("out_simple.csv", index_col='序号')
print(df2.head())

# 不能使用index_col
y = df2['收盘价']
x = df2['开盘价']

import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
fix, ax = plt.subplots()
ax.scatter(x, y, alpha=0.5)
ax.set_xlabel('开盘价')
ax.set_ylabel('收盘价')
plt.show()

# 散点图举证
from pandas.plotting import scatter_matrix

# 矩阵大小 figsize 标记 marker o是实心小圆点 透明效果 alpha
scatter_matrix(df2, figsize=(15, 15), marker='o', alpha=0.5)
plt.show()

# 相关系数
print(df2.corr())
print(df2.corr()['最高价'])
print(df2['最高价'].corr(df2['最低价']))
print('最高价和最低价的相关系数：{:.2f}'.format(df2['最高价'].corr(df2['最低价'])))