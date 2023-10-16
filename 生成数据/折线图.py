import sys
import time


# 通过run不能运行，有时候，PyCharm的Run窗口可能会有一些与IDE交互的问题。
# 可以通过terminal py *.py运行
# import matplotlib
import matplotlib.pyplot as plt

# matplotlib.use("TkAgg")
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of Value", fontsize=10)
# 设置刻度标记大小
plt.tick_params(axis="both", labelsize=14)
plt.xticks(range(0, 6, 1))
plt.yticks(range(0, 26, 1))
plt.show()
