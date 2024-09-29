# -*- coding: utf-8 -*-

# pandas 绘图函数
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

# 设置字体
mpl.rcParams['font.sans-serif'] = ['FangSong']

df = pd.read_csv("out.csv", index_col="日期")
print(df.head())
#
# x = df['日期'].values
# y = df['均值'].values
#
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

# pandas绘制折线图,还是需要show一下才能显示出图
df['开盘价'].plot(color='r')
plt.show()

# 柱形图
df['收盘价'].plot(kind='bar', color='y')
# 每plot一次就要show一次，否则会在同一个图中出现
plt.show()

df['收盘价'].plot(kind='barh', color='y')
plt.show()

# 饼图
df['均值'].plot(kind='pie')
plt.show()

# 面积图
df['金额'].plot(kind='area')
plt.show()

df.plot(kind="bar", stacked=True)
plt.show()

# 直方图
from pandas import Series

hist = Series([1, 2, 3, 4, 5, 3, 4, 2, 6, 7, 1, 3])
hist.plot(kind='hist')
plt.show()

bins = [1, 3, 5, 7]
hist = Series([1, 2, 3, 4, 5, 3, 4, 2, 6, 7, 1, 3])
hist.plot(kind='hist', bins=bins, color='r')
plt.show()