# -*- mode: python ; coding: utf-8 -*-

import matplotlib as plt
import matplotlib.pyplot as p_plt

# input_values = list(range(1, 6))
input_values = list(range(1, 100))
output_values = list(i ** 3 for i in input_values)

# 折线
# p_plt.plot(input_values, output_values, linewidth=5)
# 散点
p_plt.scatter(input_values, output_values, c=output_values, cmap=p_plt.cm.Reds, s=40)
p_plt.title("li fang", fontsize=24)
p_plt.xlabel("value", fontsize=14)
p_plt.ylabel("li fang", fontsize=14)
p_plt.tick_params(axis='both', labelsize=14)
p_plt.show()

