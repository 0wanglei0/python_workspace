# -*- coding: utf-8 -*-
import numpy as np
from pandas import DataFrame

# 随机数组
arr = np.random.randn(9)
print(arr)

# 最小
print(arr.min())

# 最大
print(arr.max())

# 均值
print(arr.mean())

# 求和
print(arr.sum())

# sort
arr.sort()
print(arr)

# 二维数组
arr1 = np.random.randn(4, 3)
print("######")
print(arr1)

# 最小 所有元素最小
print("###### min")
print(arr1.min())

# 最大 所有元素最大
print("###### max")
print(arr1.max())

# 均值
print("###### mean")
print(arr1.mean())

# 求和 所有元素和
print("###### sum")
print(arr1.sum())

# sort 每行排序
print("###### sort")
arr1.sort()
print(arr1)

print("###### sort")
# axis 按列排序
arr1.sort(axis=0)
print(arr1)

# linspace
print(np.linspace(0, 10, 2))
print(np.linspace(0, 10, 5))

# 生成0~10之间均匀分布的11个数，包括0, 10
print(np.linspace(0, 10, 11))

print("###### 线性代数")
# 线性代数
X = np.array([[1, 2, 3], [4, 5, 6]])
print(X)
y = np.array([[6, 23], [-1, 7], [8, 9]])
print(y)
print("###### dot")

# dot时，第一个矩阵的行数要与第二个矩阵的列数相同
print(X.dot(y))

from numpy.linalg import inv

m = np.array([[4, 2], [3, 1]])
# 矩阵求逆
print(inv(m))

# 随机数的生成
from numpy import random

# normal

rArray = random.normal(size=(4, 4))
print("#######")
print(rArray)

# randInt产生给定上下限范围内的随机数选取证书
# rArray = random.randint(0, 2)
rArray = random.randint(1, 10, size=(4, 4))
rArray = random.randint(0, 10)
print("#######")
print(rArray)

i = 0
while i < 10:
    print(random.randint(0, 2))
    i += 1

data = np.arange(16)

df = DataFrame(data.reshape((4, 4)), index=[1, 2, 3, 4], columns=["a", "b", "c", "d"])

# describe, 描述性统计分析
print(df.describe())
print(df.sum())  # 求和
print(df.mean())  # 均值
print(df.min())  # 最小
print(df.max())  # 最大
print(df.cumsum())  # 累计求和

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

# 非数值型的描述
print(df.describe())
