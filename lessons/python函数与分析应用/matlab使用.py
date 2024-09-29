# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# 绘图数据

import numpy as np

x = np.arange(0, 1, 0.05)
print(x)

# 正弦函数
y = np.sin(2 *np.pi * x)

# ‘b' 是颜色 --是虚线 * 是数据点 label 独立项
plt.plot(x, y, 'b--*', label='sin(x) =')
# 标题
plt.title("plot")
plt.xlabel("x")
plt.ylabel("y")
# 独立项位置 best 最适位置
# plt.legend(loc='upper left')
plt.legend(loc='best')
plt.show()

# figure和subplot
# 绘制多个图表
fig = plt.figure()
# 添加多个图表
# 第一个 必选三位数字,2行2列第一个位置
ax1 = fig.add_subplot(221)
# 第二个 2行2列第二个位置
ax2 = fig.add_subplot(222)
# 第三个 2行2列第三个位置
ax3 = fig.add_subplot(223)

# ax3.plot(x, y)

# 颜色线型和标记
# ax3.plot(x, y, 'r--*', label='sin(x)')
ax3.plot(x, y, color='b',linestyle='--', marker='o')
plt.show()

# 绘制多个图表
# fig = plt.figure()
# # 添加多个图表
# # 第一个 必选三位数字,2行2列第一个位置
# ax1 = fig.add_subplot(221)
# # 第二个 2行2列第二个位置
# ax2 = fig.add_subplot(222)
# # 第三个 2行2列第三个位置
# ax3 = fig.add_subplot(223)
# ax3 = fig.add_subplot(224)

# 简化
fig, ax = plt.subplots(2, 2)
ax[0, 1].plot(x, y, 'b--', label='sin(x) =')
plt.show()

# 标题，标签，图例
fig, ax = plt.subplots()
ax.plot(x, y, 'b--', label='sin(x)')
ax.set(xlabel='x', ylabel='y', title="subplots")
ax.legend(loc='best')
ax.grid() # 添加网格线
plt.show()

y2 = np.cos(2* np.pi * x)
print(y2)

fig, ax = plt.subplots()
ax.plot(x, y, 'b--', label='sin(x)')
ax.plot(x, y2, 'g--', label='cos(x)')
ax.set(xlabel='x', ylabel='y', title="sin&cos")
ax.legend(loc="best")
plt.show()

fig.savefig('sin&cos.png')