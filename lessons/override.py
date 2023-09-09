"""
方法重写
"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("name is {0}, age is {1}".format(self.name, self.age))

class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    # 重写方法，可不调用super方法
    def info(self):
        super().info()
        print(f"gender is {self.gender}")

    def __str__(self):
        return f"name is {self.name}, age is {self.age}, gender is {self.gender}"


stu = Student("wang", 15, "male")
stu.info()
stu.__str__()
print(stu) #未重写str之前，输出的是对象地址

"""
object类

所有类的父类，所有类都有object类的属性和方法

内置函数dir可以查看指定对象的所有属性

object有一个__str__()方法，类似于java的toString方法，为了方便查看对象信息，通常对此方法进行重写
"""

"""
多态
"""

class Animal:
    def eat(self):
        print("animal eat")

class Dog(Animal):
    def eat(self):
        print("dog eat")
class Cat(Animal):
    def eat(self):
        print("cat eat")

class People(object):

    def __init__(self, name):
        print("name is ", name, " self is ", id(self))

    def __new__(cls, *args, **kwargs):
        print("cls is ", id(cls))
        obj = super().__new__(cls)
        print("obj is ", id(obj))
        return obj

    @classmethod
    def eat(cls):
        print("person eat")

def fun(animal):
    animal.eat()

def fun1(any_object):
    any_object.eat()

fun(Dog())
fun(Cat())
fun(Animal())

# 因为python是动态语言，java是静态语言，静态语言实现多态的三个必要条件：1.继承 2.方法重写 3. 父类引用指向子类对象
# 因为People中有eat行为，因此当people作为参数调用fun时，仍然可以使用
fun(People("a"))

fun1(Dog())
fun1(Cat())
fun1(Animal())
fun1(People("a"))


"""
特殊属性
__dict__  获取类对象或实例对象所有的属性和方法的字典

特殊方法
__len__   获取对象的长度，可以重写，默认用于列表等
__add__   可以自定义 "+" 功能,默认是加法动作，类似c++的operator
__new__   用于创建对象  创建对象先执行new之后执行init初始化
__init__  对象初始化
"""

print(dir(Student))
print(stu.__dict__)
print(stu.__class__)
print(Student.__dict__)
print(Student.__le__)
a = 10
print(a.__add__(10))

b = (1,2,3)
print(b.__len__())

c = {"a", "b", "c"}
print(len(c))


print("object id is ", id(object))
print("People id is ", id(People))

people = People("b")
print("people id is ", id(people))