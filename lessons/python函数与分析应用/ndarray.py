# -*- coding: utf-8 -*-
import numpy as np

# ndarray

# 创建数组 array

data1 = [1, 2, 3]
arr1 = np.array(data1)  # 一维数组
print(arr1)

# 创建多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
arr2 = np.array(data2)
print(arr2)

# dtype 数据类型
arr2.dtype

# shape 属性
arr2.shape

arr2 = np.array(data2, dtype=np.int64)
print(arr2)
print(arr2.dtype)

# float 数组
data3 = [6, 7.5, 8, 0, 3.2]
arr3 = np.array(data3)
print(arr3)
print(arr3.dtype)

# 类型转换 astype
print(arr3.astype(np.int64))

# ones 全为1的数组
print(np.ones(10))

# zeros 全为0的数组 一维数组
print(np.ones(10))

# zeros 全为0的数组 二维数组
print(np.ones((3, 6)))
