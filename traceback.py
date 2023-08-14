# import traceback
#
# """
# 使用traceback打印异常信息
#
# """
#
# try:
#     num = 10 / 0
# except BaseException as e:
#     print(traceback)
# finally:
#     print("over")


"""
Pycharm调试

断点
"""

"""
·面向过程

·面向对象

·类和对象创建
1.类的声明
class student:
    变量
    静态方法
    类方法
    无注解方法
    初始化方法
    pass
2.类的创建
student = Student(参数)


·类方法和静态方法
"""


def method():
    print("normal method")


class Student: # 一般首字母大写
    name = ""
    age = 0
    gender = "male"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod # 静态方法，不需要添加self参数 注解声明是静态方法
    def eat():
        print("students eat")

    @classmethod # 注解声明是类方法，一般参数为cls
    def run(cls):
        print("students run")


# 类内定义为方法，类外定义为函数
def drink():
    print("drink")

# 声明的对象可以直接调用方法
student = Student("wang", 12, "male")

print(id(student))
print(type(student))
print(student)
print(student.age)
print(student.name)
print(student.gender)
student.eat()
student.run()
method()
print("-------------------------")
print(id(Student))
print(type(Student))
print(Student)
print(Student.age)
print(Student.name)
print(Student.gender)
Student.eat() # 静态方法不传入参数
method() # 方法需要参数
Student.run() # 注解声明的方法不传入参数


"""
动态绑定属性和方法
def show():
    print()
stu.show = show
stu.show()
"""

# 可以直接添加属性，但只对当前对象有用，此过程为动态绑定，相当于多态吧
student.home = "where"
print(student.home)

# 动态绑定方法，多态，覆盖
student.eat = drink
student.eat()

