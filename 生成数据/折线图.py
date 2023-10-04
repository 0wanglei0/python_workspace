import sys
import time


# 通过run不能运行，有时候，PyCharm的Run窗口可能会有一些与IDE交互的问题。
# 可以通过terminal py *.py运行
# import matplotlib
import matplotlib.pyplot as plt

# matplotlib.use("TkAgg")
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()

time.sleep(10)
sys.exit()
