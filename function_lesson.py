"""
function

函数返回值如果是多个值，那么结果是元组

"""


def fun(numbers):
    result_odd = []
    result_not_odd = []
    for item in numbers:
        if not item % 2:
            result_odd.append(item)
        else:
            result_not_odd.append(item)
    return result_odd, result_not_odd


print(fun(range(10)))

"""
如果函数执行没有返回值，则return可以省略

如果函数执行有一个返回值，则return对应类型

如果函数执行多个返回值，则return类型为元组


函数参数定义
定义默认值函数
def fun(a, b = 10)

个数可变的位置参数
·无法确定传递的参数个数，使用*定义参数
·入参为一个元组
·def fun(*args)


个数可变的关键字参数
·使用**定义个数可变的关键字参数
·入参为字典
·def fun(**args)

如果同时存在以上两种参数，位置参数要在关键字参数之前
"""


def fun1(*args):
    print(args)


fun1("hello", "python")


def fun2(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)


lst = [1, 2, 3]
# 将列表转换为位置参数
fun2(*lst)

dictionary = {"a": 4, "b": 5, "c": 6}
# 将字典转换为关键字参数
fun2(**dictionary)


# *之后只能通过关键字参数进行传递
def fun3(a, b, *, c, d):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)


fun3(1, 2, c=3, d=4)
