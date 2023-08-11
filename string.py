"""
字符串的驻留机制

新建的字符串开辟空间，之后的同样的只是指向引用

驻留机制的集中情况

·字符串的长度是0或1时
·符合标识符的字符串
·字符串只在编译时进行驻留，而非运行时
·[-5, 256]之间的整数数字  在pycharm中优化了 ，但是在python命令行中2.7版本 此条件有效

sys中的intern方法强制2个字符串指向同一个对象
Pycharm对字符串进行了优化处理

驻留机制的优缺点：
1.避免频繁创建和销毁，提升效率和节约内存
2.字符串拼接建议使用join方法，而非+，join方法是先计算字符中的长度再拷贝，值new一次对象，效率比+高
"""

a = "abc"
b = "ab" + "c"
c = "".join([a, b])
print(id(a))
print(id(b))
print(id(c))

a = -6
b = -6
print(a is b)

"""
字符串的查询操作

1.index  查找子串的第一次出现位置，不存在时抛出异常
2.rindex 查找子串的最后一次出现位置，不存在时抛出异常
3.find   查找子串的第一次出现位置，不存在时返回-1
4.rfind  查找子串的最后一次出现位置，不存在时返回-1
"""
s = "new python"
print(s.index("ew"))
print(s.rindex("on"))
print(s.find("ex"))
print(s.rfind("new"))

"""
字符串大小写转换

upper 都转换成大写
lower 都转换成小写
swapcase 大小写转换
capitalize 第一个字符大写，其余转换为小写
title 每个单次首字母大写，其余小写

不改变原字符串
"""
print(s.upper())
print(s)
print(s.lower())
print(s)
print(s.swapcase())
print(s)
s = "aBsc Dsa"
print(s.capitalize())
print(s)
s = "aBsc Dsa"
print(s.title())
print(s)

"""
字符串对齐操作

center 居中对齐，第一个参数指定宽度，第二个参数指定填充符，默认是空格，如果设置的宽度小于实际宽度，返回原字符串
ljust 左对齐，第一个参数指定宽度，第二个参数指定填充符，默认是空格，如果设置的宽度小于实际宽度，返回原字符串
rjust 右对齐，第一个参数指定宽度，第二个参数指定填充符，默认是空格，如果设置的宽度小于实际宽度，返回原字符串
zfill 右对齐，左边用0填充，该方法只接收一个参数，指定字符串宽，如果设置的宽度小于实际宽度，返回原字符串
"""
s = "hello python"
print(s.center(30, "*"))
print(s.ljust(10))
print(s.rjust(20, "-"))
print(s.zfill(20))
print("-123".zfill(20)) #负数会在符号之后补0

"""
字符串拆分

split() 默认拆分字符是空格，返回值是列表  参数sep指定分隔符  maxsplit指定分隔的最大次数，大于最大次数时，剩余部分单独为一个
rsplit() 与split相同，不同的是从右开始分割
"""
print(s.split(sep=" ", ))
print(s.rsplit("o", 1))

"""
字符串常用操作方法

1.isidentifier 判断字符是否为合法标识符
2.isspace 判断是否全部由空白字符组成，包括回车、换行、水平制表符tab
3.isalpha 是否由全字母组成
4.isdecimal 是否为十进制数组组成
5.isnumeric 是否全部是数字组成
6.isalnum 是否为字母和数字组成
7.replace 第一个参数指定被替换的子串，第二个参数指定替换后的字符串，第三个参数指定替换的次数（可能会有多个相同参数）,不改变原有字符串
8.join 将列表或元组的字符串合并为一个字符串,字符串被视为列表,需要元素是str
"""

s = "a a a a a "
print(s.replace("a", "b"))
print(s.replace("a", "b", 3))
print(s)

print(s.join(("1", "2")))
print(s.join(["1", "2"]))


"""
字符串的比较

1.运算符：> >= < <= == !=
2.比较规则：从第一个字符开始比较两个字符串，直到两个字符串的字符不一致，后续字符不再比较
3.原理：两个字符比较时，比较的是ordinal value，调用内置函数ord可以得到指定字符的ordinal value，与ord对应的函数是chr，可以
通过ordinal value获取到对应字符

== 比较的是value
is 比较的是地址

切片操作
字符串时不可变类型，不能增删改，切片将产生新对象
与列表类似
string[start:stop:step]
如果是负数，从字符串的start开始截取

"""
s = "hello, python"
print(s[-5::1]) #从y开始截取

"""
格式化字符串
两种方式
1.%
%d, %s, %i, %f...
2.{}
{0}, {1}
s = "{0},{1}".format(value, value1)
s = f"a{value}, b{value1}"
....{0}, ....{1}, {0}.format()
"""

name = "wang"
age = "3"
print("my name is {0}, age is {1}".format(name, age))
print(f"my name is {name}, age is {age}")

print("%10d" % 99) # 10表示宽度
print("%10.3f" % 3.1415926) # 3表示精度，10表示宽度

print("{0:.3}".format(3.1415926)) #此处3表示总长度
print("{0:.3f}".format(3.1415926)) #此处3表示3位小数
print("{:10.3f}".format(3.1415926)) # 只有一个参数，0可省略，此处3表示3位小数,10表示宽度


"""
字符串的编码转换
"""

s = "你好"
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8"))
print(s.encode("utf-8").decode("gbk"))
print(s.encode("gbk"))
print(s.encode("gbk").decode("gbk"))