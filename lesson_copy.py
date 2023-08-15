"""
深拷贝
使用copy.deepcopy()拷贝，拷贝对象和子对象都不相同，指向不同的对象

浅拷贝
使用copy.copy()拷贝时，原对象和拷贝对象会使用同一个对象
"""

class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = CPU()
cpu2 = cpu1 # 类对象的复制操作

print(cpu1)
print(cpu2)

disk = Disk()

computer = Computer(cpu1, disk)
import copy
computer2 = copy.copy(computer)
computer3 = copy.deepcopy(computer)

print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)
print(computer3, computer3.cpu, computer3.disk)