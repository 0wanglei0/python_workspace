"""
变量的作用域

局部变量
函数内部定义的变量，如果局部变量使用global声明，就成为全局变量

全局变量
"""

# 预先定义和初始化
age = 10
def fun():
    # 使用全局变量，再修改age的值会改变外部变量
    global age
    # 修改变量的值
    age = 20
    print(age) # 20

# 需要调用才会实际对age起作用
fun()
# 此处输出为函数内被改变的值
print(age)


"""
递归函数

递归函数每调用一次，都会在栈内分配一个栈帧
执行完函数，释放相应的空间
优点：代码简单，逻辑清晰
缺点：占用内存多，效率低
"""

def fac(number):
    if number == 1:
        return 1
    else:
        return number * fac(number - 1)

print(fac(6))


"""
实现斐波那契数列

"""

def fib(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

# 此处会沉默，无输出结果
# print(fib(1000))

# 用for循环会很快输出
result = 1
for i in range(1000):
    if i == 0:
        result = 1
    elif i == 1:
        result = 1
    else:
        result = (i - 1) * (i - 2)

print(result)


"""
bug

·不同类型的处理方式
1.语法错误 syntaxError
2.索引越界 indexError
3.keyError
4.NameError
5.ValueError
6.ZeroDivisionError


异常处理机制:先子类，后父类的顺序，最后增加BaseException
try:
    statement
except Error:
    statement1
except Error:
    statement1
except BaseException [as e]:
# 异常进入
    statement1
else:
# 非异常进入
    statement1
finally:
# 都会进入
    statement1
    

pycharm的调试模式
"""

try:
    a = int(input("please input number"))
    b = int(input("please input number"))
    result = a / b
    print(result)
except BaseException as e:
    print(e)
else:
    print("result is {0:.3f}".format(result))
    print("result is %.3f" % result)
finally:
    print("over")