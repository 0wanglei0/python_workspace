from 生成数据.demo_randomwalk import RandomWalk
import pygal

rw = RandomWalk(50000)
rw.fill_walk()

hist = pygal.XY(stroke=False)
hist.title = "Results of Rolling one D6 1000 times"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("point", [(rw.x_values[i], rw.y_values[i]) for i in range(len(rw.x_values))])
hist.render_to_file("random_walk.svg")
