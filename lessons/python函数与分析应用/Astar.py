# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt


class MyQ:
    def __init__(self):
        self.lt = []

    def push(self, t):
        self.lt.append(t)
        self.lt.sort(key=lambda x: (x[1], x[2]), reverse=True)

    def pop(self):
        return self.lt.pop()[0]

    def __len__(self):
        return len(self.lt)


class Astar:
    def __init__(self, w, h, s, g, wall):
        self.w, self.h = w, h
        self.s, self.g = s, g
        self.wall = np.array(wall).T
        self.data = np.zeros((w, h))
        self.data[s] = 1
        self.data[g] = 1
        self.data[wall] = 2
        self.que = MyQ()
        self.que.push((s, 0, 0))

    def find_path(self):
        cost_g = {}
        parent = {}
        parent[self.s] = None
        cost_g[self.s] = 0
        while self.que:
            current = self.que.pop()
            if current == self.g:
                break
            for node in self.negi(current):
                new_cost_g = cost_g[current] + 1
                if node not in cost_g or cost_g[node] > new_cost_g:
                    cost_g[node] = new_cost_g
                    h = abs(node[0] - self.g[0] + abs(node[1] - self.g[1]))
                    self.que.push((node, new_cost_g + h, h))
                    self.data[node] = 3
                    parent[node] = current

            self.draw_path(parent)

    def draw_path(self, parent):
        g = self.g
        while g:
            self.data[g] = 4
            g = parent.get(g)
            print(g)

        self.data[self.s] = 1
        self.data[self.g] = 1
        # self.plot()

    def negi(self, node):
        lt = []
        for i in [-1, 1]:
            if node[0] + i >= 0 and node[0] + i < self.w:
                new_node = node[0] + i, node[1]
                if self.check(new_node): lt.append(new_node)
            if node[1] + i >= 0 and node[1] + i < self.h:
                new_node = node[0], node[1] + i
                if self.check(new_node): lt.append(new_node)
        return lt

    def check(self, node):
        b = np.all(self.wall == node, axis=1)
        return not np.any(b)

    def plot(self):
        a = plt.pcolor(self.data)
        a.set_edgecolor('w')
        plt.gca().set_aspect(1.0)
        plt.show()


wall = (np.array(range(9)), np.array([10] * 9))
print(wall)
a = Astar(20, 30, (0, 0), (12, 24), wall)
a.find_path()
a.plot()
