import random

year = eval(input("please input year "))
#
# while len(year) != 4:
#     year = eval(input("please re input year"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is run")
else:
    print(year, "is ping year")

yes_or_no = "y"
over_flag = False


def cycler(number):
    if number == 1:
        print("当前金额为1123")
    elif number == 2:
        print("当前剩余流量为123GB")
    elif number == 3:
        print("当前剩余通话时间5分钟")
    elif number == 0:
        global over_flag
        over_flag = True
    else:
        print("sorry, the number is not support")
        re_input = eval(input("please re input: "))
        cycler(re_input)


while yes_or_no == "y":
    print("--------欢迎使用10085查询功能--------")
    print("1.查询当前余额")
    print("2.查询当前剩余流量")
    print("3.查询当前剩余通话时间")
    print("4.退出系统")
    intput_number = eval(input("请输入要执行的操作： "))
    cycler(intput_number)
    if over_flag:
        break
    next_one = input("是否继续查询: ")
    yes_or_no = next_one

print("程序退出，谢谢您的使用")

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "X", i, "=", i * j, end="\t")
    print()
print()

"""
随机数
random.randInt(1, 100)包含1~100

"""
number = random.randint(1, 100)
count = 0
while count < 10:
    input_number = eval(input("please guess :"))
    if input_number == number:
        count += 1
        print("you win")
        break
    elif input_number > number:
        print("big")
    else:
        print("small")
    count += 1

if count <= 3:
    print("you are clever, 猜了", count)
elif count <= 6:
    print("you are clever, 猜了", count)
else:
    print("you are lucky, 猜了", count)

"""
空语句 pass

不做任何事，起到占位符的作用，一般可用在if、for、while、函数的定义、类的定义中
"""

if True:
    pass
    print("test pass")
