# -*- coding: utf-8 -*-
# 基本索引和切片
import numpy as np

# arange range的数组版
print(np.arange(10))

nd1 = np.arange(1, 20, 2)
print(nd1)

nd1[2:5] = 10
print(nd1)

# 多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
nd = np.array(data2)

print(nd[0][2])
print(nd[0, 2])

# 花式索引 Fancy indexing
nd = np.arange(32)
print(nd)

# nd1 的new shape 要nd能整除
nd1 = np.reshape(nd, (8, 4))

# 常规索引
print(nd1[0])

# 花式索引 nd1传入一个数组,数组为对应的索引，可以获得多行元素
print(nd1[[1, 2, 4, 3]])

# 选取多行多列，交叉处的元素,第一个数组代表行索引，第二个数组代表列索引
# 行列下标一一对应
print(nd1[[1, 2, 3, 5], [0, 3, 2, 1]])

# 获取一个矩形区域怎么办
# 获取矩形区域，第一种方法
print('#################')
print(nd1[[1, 4, 5, 2]][: ,[3, 1, 0, 2]])

print('#################')
# 第二种方法 np.ix_
print(nd1[np.ix_([1, 5, 2, 7], [0, 3, 2, 1])])
