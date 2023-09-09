import unittest


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def give_raise(self, raise_salary=5000):
        self.salary += raise_salary
        return self.salary


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("wang", 30, 10000)

    def test_give_default_raise(self):
        default_salary = self.employee.give_raise()
        assertEquals(default_salary, 15000)

    def test_give_custom_raise(self):
        custom_salary = self.employee.give_raise(500)
        assertEquals(custom_salary, 10500)


unittest.main()
