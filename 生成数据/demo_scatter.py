# 15.2.3 使用scatter绘制散点图并设置样式

import matplotlib.pyplot as plt

input_values = [i for i in range(1, 11)]
# input_values = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in input_values]
# squares = [1, 4, 9, 16, 25]
# edgecolors 边缘颜色  c 数据点颜色,可以直接赋值颜色"red", 也可以使用(0, 255, 128)RGB设置颜色,
# cmap 设置颜色映射,设置c为数据源，cmap为对应的渐变颜色,由浅到深，所有颜色映射访问http://matplotlib.org/
plt.scatter(input_values, squares, c=squares, edgecolors='none', cmap=plt.cm.Blues, s=10)
plt.title("Square Numbers Scatter", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 101, 10))
plt.tick_params(axis='both', which='major', labelsize=14)
# 此处书上写的是[],但是此处提示要用元组或字符串等其他格式
plt.axis((0, 11, 0, 110))
# plt.show()
# 自动保存图表,第二个参数去掉多余的空白
plt.savefig("squares_plot.png", bbox_inches="tight")
