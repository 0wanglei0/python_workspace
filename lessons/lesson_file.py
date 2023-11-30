"""
编码格式：UTF-8 Unicode

文件读写原理

俗称 IO操作

文件读写流程
打开或新建文件
open

file = open(filename [, mode, encoding])
文件对象   打开文件函数    文件名    模式，默认只读    编码格式，默认格式是GBK
读写
关闭文件


操作原理

"""
# encoding="utf-8"

# file = open("test.txt", "a+", encoding="utf8")
# file = open("test.txt", "r+", encoding="utf8") # r+ 会覆盖掉新输入部分大小空间的内容
file = open("../test.txt", "a+", encoding="utf8") # 2+ 会覆盖掉全部内容，重新写入
print(file.read())
print(file.encoding)
file.write("lalalalala\n")
file.writelines("nananna\n")
file.flush()
file.seek(3) # w+、a+ 模式光标要在开头才能读取
# print(file.read())
print(file.tell())
print(file.readlines())
file.close()

"""
常用的文件打开模式

文件分为：文本文件、二进制文件

打开模式：
r 读
w 写
a 追加 文件不存在则新建
b 二进制方式打开文件，需要与其他模式一起使用,rb,wb
+ 以读写的方式打开文件，不能单独使用，例如 a+


文件对象常用方法

read        读取文件，参数size可设置读取的size，默认读取到末尾
readline    读取行
readlines   读取行返回list
write       写文件
writelines  写入行
seek        移动光标
tell        当前光标位置
flush       缓冲去内容刷到文件中，直接写入，不关闭文件
close       写入文件，关闭文件
"""
a = 0
if a:
    src = open("../马士兵课程/python/socket编程/code_net/source.png", "rb")

    target = open("../target_file.png", "wb")

    target.write(src.read())

    src.close()
    target.close()


"""
with语句

自动管理上下文资源，确保文件可以正确关闭，释放资源
"""

with open("../target_file.png", "rb") as src:
    src.read() # 此处可以不用关闭，会自动关闭


# 实现了enter/exit, 就遵守了上下文协议，那么该类的实例对象被称为上下文管理器
class MyContextMgr(object):
    def __enter__(self):
        print("join enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 上下文协议，即使出现异常也会执行退出方法
        print("join exit")

    @classmethod
    def show(cls):
        print("join show")

with MyContextMgr() as file:
    file.show()


"""
目录操作

os模块语句执行结果与操作系统有关，不同结果可能会有不同的结果

os.path 操作文件和目录

getcwd      获取当前工作目录
listdir(path)   返回指定路径下的文件和目录信息
mkdir(path[, mode])     创建目录
makedirs(path1/path2...[, mode])    创建多级目录
rmdir(path)         删除文件夹
removedirs(path1/path2...)      删除多级目录
chdir(path)             将path设置为当前工作目录
"""

import os

# 命令
if a:
    os.system("notepad.exe")
    os.system("calc.exe")

    # 直接调用可执行文件
    os.startfile("C:/Users/pc/AppData/Local/GitHubDesktop/GitHubDesktop.exe")

print(os.getcwd())
lst = os.listdir('')
print(lst)

# os.chdir("D:/python_workspace")
# print(os.getcwd())

"""
os.path操作目录

abspath(path)       获取文件或目录的绝对路径
exists(path)        文件或目录是否存在
join(path, name)    将目录与目录或文件名拼接起来
splitext()          分离文件名和扩展名
basename(path)      从目录中提取文件名
dirname(path)       从路径中提取文件路径，不包括文件名
isdir(path)         判断是否为路径
"""

import os.path

print(os.path.abspath("lesson_file.py"))
print(os.path.exists("lesson_file.py"))
print(os.path.join("", "lesson_file.py"))
print(os.path.splitext("lesson_file.py")[1].split(".")[1])
print(os.path.basename("D:/python_workspace/lesson_file.py"))
print(os.path.dirname("D:/python_workspace/lesson_file.py"))
print(os.path.isdir("lesson_file.py"))

path = os.getcwd()

# 遍历当前目录下的所有目录及文件展示出来
lst1 = os.walk(path)
for dirpath, dirname, filename in lst1:
    print(dirpath)
    print(dirname)
    print(filename)

lst = os.listdir(path)
print(os.listdir(path))

for filename in lst:
    if filename.endswith(".py"):
        print(filename)