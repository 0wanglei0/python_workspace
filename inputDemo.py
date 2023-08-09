# doc

"""
coding:utf-8
注释
"""
# fp = open("test.txt", "w")
# print("life is short", "I use python", sep=", ", end="", file=fp)
# fp.close()

# print("-------Introduction-------\n",
#     "name：", input("please input your name: "), "\n",
#     "age：", input("please input your age: "), "\n",
#     "motto：", input("please input your sign: "), "\n")

import keyword
"""
print 可设置分隔符、换行符、输出到文件
可使用， + 来拼接字符串
保留字
查看保留字：
 import keyboard
 keyword kwlist
and  as assert break  class continue
def  del elif else except finally
for from False global if import
in is lambda nonlocal not none
or pass raise return try True
while with yield
"""
true = 1

print(keyword.kwlist)
print(keyword.softkwlist)
print(0b101)
print(0O101)
print(0x101)
print(2/3)
print(0.2+0.1)
print(round(0.2+0.1111111,4))


"""
字符串索引
反向索引
-5  -4    -3   -2    -1
h    e     l    l     o
0    1     2    3     4
正向索引


截取字符串指定区域

string[1:2]  含头不含尾 string[1:-3]
1,2均可为空

x+y 字符串连接
x*n 复制字符串 n代表复制次数
y in x y在x中？

"""
string = "12345"
print(string[-2])
print(string[2])
print(string[0:2])
print("echo " + string[1:-3]) # 2
print(string[:])
print(string+string[2])
print(string*int(string[2]))
print(string[2] in string)

"""
复数类型
复数由实部和虚部组成
j是复数的一个基本单位，被定义为j=根号-1，又称虚数单位
.real获取实数部分，.imag获取虚数部分
"""
x = 123+456j
print(x.real)
print(x.imag)
print(r'\n')
print(R'\\n')

"""
数据类型转换
隐式转换
通过数学运算进行转换

显式转换
int(x) int
float(x) float
str(x) 字符串
chr(x) 字符
ord(x) ASCII码
hex(x) 16进制
oct(x) 8进制
bin(x) 2进制
"""

a = 2
b = 2.0

print(int(b))
print(float(a))
print(str(a))
print(chr(a))
print(type(a))
print(ord(str(a)))
print(hex(a))
print(oct(a))
print(bin(a))


"""
eval()函数

去掉字符串最外侧的引号，经常和input函数一起使用，获取用户输入的数值型
"""

print(string, type(string), type(eval(string)))
print(type(eval(input("age is "))))
s="test"
print(eval("s"))

print(True + 1)  # =2
print(bool(1)) # true
print(bool(0)) #false 所有非0类型的布尔值都为true


"""
运算符

+ - * / //（整除） ** （幂运算）

"""


"""
赋值

"""
a,b = 10, 20
a, b = b, a #赋值互换

"""
逻辑运算符

and 与  如果第一个表达式为false 不会执行第二个表达式
or 或   当第一个表达式为true时，不会执行第二个表达式
not 非
"""

"""
位运算符

&   12&8 = 8    1100 & 1000 = 1000 = 8
|   12&2 = 12   1100 | 0010 = 1110 = 14
^ 异或 按位相同为0，不同为1   12^8   1100 ^ 1000 = 0100 = 4
~ 取反 按位1为0,0为1 ~12 1100 ~1100 = 0011 = 3
<< 左移位 按位左移，溢出舍弃，空位补0  4 << 1 = 0100 << 1 = 1000 = 8
>> 右移位 按位右移，右侧溢出舍弃，左侧空位,如果最高位为1，空位补1，如果最高位为0，空位补0
  4 >> 3 = 0100 << 3 = 1111
  
  -4 >> 3
  1100
  1111
"""
print(bin(4 << 3))
print(bin(4 >> 3))
print(bin(-4 >> 3))
print((-4 >> 3))
print(bin(-4))


"""
运算符优先级

** 幂
~ + - 正负
* / % // + -  算数 
<< >> 位移
&  位与
^  异或
|  位或
比较运算符
"""

inputString = input("please input number")
number = eval(inputString)
four = number // 1000
three = number % 1000 // 100
two = number % 1000 % 100 // 10
one = number % 1000 % 100 % 10

sd = number % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000


print("one is ", one)
print("two is ", int(two))
print("three is ", three)
print("four is ", four)

print("sd is ", sd)
print("ten is ", int(ten))
print("hundred is ", hundred)
print("thousand is ", thousand)

f_height = float(input("input father height : "))
m_height = float(input("input mother height : "))

s_height = (f_height + m_height) * 0.54
print("s_height is : ", round(s_height, 2))


"""
链式赋值
a, b, c, d = 100

元组分解赋值
name1, age1 = "aaa", 20

列表分解赋值
[name2, age2] = ["bbb", 3]

字符串分解赋值
a, b, c, d = "room"
a="r" ...

扩展字符串解包赋值
a, *b = "room"
a = "r"
b="oom"
"""

"""
条件语句 if
and or
"""
n = 3
if n%2:
    print("1")
if not n%2:
    print("0")

if n%2:print("1")

#条件表达式 变量赋值的方式，类似于三项表达式
result = "result" if n == 2 else "no result"
print(result)

"""
遍历循环for
  for n in s:
    statement
    
遍历循环扩展模式
for 循环变量 in s:
  statement
else: # 只在循环正常结束后执行，通常与continue、break结合使用，break不算正常结束
  statement
  
无限循环while
while n:
  statement
else: ## 扩展模式，break不算正常结束
  statement
"""

file = open("test.txt", "r", encoding="utf-8")
for line in file:
    print(line)

for i in "hello":
    print(i)

# range() 生成一个[n,m)的整数序列
for i in range(1, 11):
    if i % 2 ==0:
        print("odd")
        break
    print(i)
    i+=1
else:
    print("555")

for i in range(100, 1000):
    m = i // 10 % 10 # 十位
    n = i % 10  # 个位
    k = i // 100      #百位
    number = m ** 3 + n **3 + k **3
    if number == i:
        print("水仙花: ", i)

i = 0
while i < 3:
    if i == 2:
        print("a", i)
        break
    else:
        print("b", i)
        i+=1
else:
    print("A")