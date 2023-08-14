"""
函数定义
[]为可选
def 函数名([输入参数]):
    函数体
    [return 结果]

函数的调用
result = 函数名(参数)

"""

def add(a=2, b=1):
    return a + b

print(add())
print(add(b=2, a=2))