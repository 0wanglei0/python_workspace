"""
·封装
1.私有属性使用 __value

·继承
提高复用
1.格式：class 子类(父类1，父类2，...):
    pass
2.如果一个类没有继承任何类，默认继承object
3.支持多继承，定义子类时，必须在构造函数中调用父类的构造函数

·方法重写

·object类

·多态
1.提高扩展和可维护性

·特殊方法和特殊属性

"""

class Car:
    name = "CHANGAN"
    __cid = "64SDFGS56"

    def getCId(self):
        return self.__cid

    def setCId(self, cid):
        self.__cid = cid


print(Car.name)
car = Car()

print(dir(car)) # 显示所有可调用的
print(car._Car__cid) # 可以调用私有的属性，Python的私有不是完全控制不能访问，要靠自觉

print(car.getCId())


class Person(object):
    def __init__(self, name, age):
        print("in Person")
        self.name = name
        self.age = age

    def info(self):
        print(f"姓名{self.name}, 年龄{self.age}")

class Teacher(Person):
    def __init__(self, name, age, gender):
        print("in Teacher")
        super().__init__(name, age)
        self.gender = gender

class B(Person):
    def __init__(self, name, age, score, other):
        print("in B")
        super().__init__(name, age)
        self.score = score
        self.other = other

# 尽量不使用多继承
class C(B, Teacher):
    def __init__(self, name, age, gender, score, other):
        print("start")
        # 在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照MRO（Method Resolution Order）：方法解析顺序进行的
        super(B, self).__init__(name, age, gender) # 只能super一个,并且要指定第一个,要用参数多的那个？
        super(Teacher, self).__init__(name, age)
        self.name = name


person = Person("li", 16)
teacher = Teacher("wang", 16, "male")
teacher.info()
person.info()

print("-----------------------------------")
c = C("c", 12, "female", 10, "c")
c.info()

print(C.__base__)
print(C.__bases__)
print(C.__mro__)
