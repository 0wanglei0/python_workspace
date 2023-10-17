import matplotlib.pyplot as plt

from demo_randomwalk import RandomWalk

# while True:
rw = RandomWalk(50000)
rw.fill_walk()

plt.figure(dpi=128, figsize=(10, 6))
point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=1)

plt.scatter(0, 0, c="green", edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors='none', s=100)

# 练习1
# plt.plot(rw.x_values, rw.y_values, linewidth=12)
# TODO 没实现隐藏坐标轴，网上找的方式也没有实现
# fig = plt.figure()
# fig.gca().spines['top'].set_visible(False)
# fig.gca().spines['bottom'].set_visible(False)
# fig.gca().spines['left'].set_visible(False)
# fig.gca().spines['right'].set_visible(False)
# plt.axes().get_xaxis().set_visible(True)
# plt.axes().get_yaxis().set_visible(True)
plt.show()
#
# keep_running = input("Make another walk？（y/n）")
# if keep_running == "n":
#     break
