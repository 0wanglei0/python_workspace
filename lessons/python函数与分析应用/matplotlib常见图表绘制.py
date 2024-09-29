# -*- coding: utf-8 -*-

# 常用图表绘制

# 读取数据
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("out.csv")
print(df.head())

x = df["日期"].values

from pylab import mpl

# 设置字体
mpl.rcParams['font.sans-serif'] = ['FangSong']
y = df["开盘价"].values
print(x)
print(y)
# 折线图
fig, ax = plt.subplots()
ax.plot(x, y, 'r')
ax.set(title="开盘价走势", xlabel="time", ylabel="price")
plt.show()

# 柱形图 & 条形图
fig, ax = plt.subplots()
# 0.5 间距
# 柱形图
# ax.bar(x, y, 0.5, color='skyblue')
# 水平图或条形图
ax.barh(x, y, 0.5, color='skyblue')
ax.set(title="开盘价走势", xlabel="time", ylabel="price")
ax.set_title("开盘价")
ax.set_xlabel("time")
# ax.set_xticks()
plt.show()

# 饼图
fig, ax = plt.subplots()
# explode 间距
ax.pie(y, labels=x, autopct='%1.1f%%', explode=[0, 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125])
plt.show()

# 散点图
# index_col 是设置index列，读取后不能使用了
scatter_df = pd.read_csv("out.csv")
print(scatter_df.head())
fig, ax = plt.subplots()
x = scatter_df["日期"]
y = scatter_df["收盘价"]
print(x.head())
print(y.head())
ax.scatter(x, y, alpha=0.5, color='r')
ax.set(title="散点图", xlabel="time", ylabel="price")
plt.show()