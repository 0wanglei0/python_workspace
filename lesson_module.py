"""
模块
1.一个模块中有多个函数

2.一个python文件就是一个模块

3.模块好处
·方便其他程序与脚本导入使用
·避免函数名和变量名冲突
·提高代码的可维护性和重用性

自定义模块
1.每一个.py文件，尽量别与自带标准模块名相同

导入模块
import module [as lias]

from module import 函数/变量/类

"""

import math
import time

import variable as v
from lesson_copy import Computer, CPU, Disk

print(v.fac(10))
print(math.pi)

computer = Computer(CPU(), Disk())
print(computer)


"""
已主程序形式运行


"""
# 只能导入包名或模块名
import lessons.test as m
# 可以导入包名、模块名、函数、变量


# 只有执行的是当前文件时，才会执行下记方法，避免执行引入模块的代码
if __name__ == '__main__':
    print("start")
    m.fun()


"""
Python中的包
包和目录的区别：
包含__init__.py文件的目录成为包
目录中不包含上记的文件

包的引入
import 包名.module

from 包名.module import fun


常用的内置模块
sys  与python解释器及环境相关的标准库
time 提供与时间相关的各种函数标准库
os   提供了防伪操作系统服务功能的标准库
calendar 日期有关的各种函数标准库
urllib 用于读取网络的数据标准库
json   json序列化和反序列化
re 用于在字符串中执行正则表达式匹配和替换
math   标准运算符函数的标准库
decimal  进行精确控制运算精度，有效位数和四舍五入操作的十进制运算
logging  日志功能
"""

import sys
import re

sys.exc_info()
# os.open("C://", flags=0)
re.escape("\n")


"""
模块的安装

在线安装：pip install 模块名
"""

import schedule


def job():
    print("job start")

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

