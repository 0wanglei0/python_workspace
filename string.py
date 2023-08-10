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
sfill 居中对齐，第一个参数指定宽度，第二个参数指定填充符，默认是空格，如果设置的宽度小于实际宽度，返回原字符串
"""