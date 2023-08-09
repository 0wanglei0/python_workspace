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
    print("you are clever, 猜了", count, "次")
elif count <= 6:
    print("you are clever, 猜了", count, "次")
else:
    print("you are lucky, 猜了", count, "次")

"""
空语句 pass

不做任何事，起到占位符的作用，一般可用在if、for、while、函数的定义、类的定义中
"""

if True:
    pass
    print("test pass")


"""
实现人机对战：石头剪刀布

需求：
分析人物角色
·玩家输入 ： 1-》拳头  2-》剪刀  3-》布
·电脑输出 同样，使用random.randint(1,3)

程序处理
·使用多重if判断玩家与电脑角色输赢情况
·使用无限循环while实现多局对战

绘制流程图

增加变量保存当前数字对应的值，只要判断赢就可以了，其余都是输，直接输出值
"""

continue_flag="y"
while continue_flag == "y":
    print("-------")
    player_number = eval(input("请玩家出 1.石头 2.剪刀 3.布： "))
    computer_number = random.randint(1, 3)
    if player_number == computer_number:
        print("玩家与电脑 平 ", player_number)
    elif player_number == 1 and computer_number == 2:
        print("玩家出拳", player_number, ", 电脑出剪刀", computer_number, " 玩家胜")
    elif player_number == 1 and computer_number == 3:
        print("玩家出拳", player_number, ", 电脑出布", computer_number, "玩家负")
    elif player_number == 2 and computer_number == 1:
        print("玩家出剪刀", player_number, ", 电脑出拳", computer_number, "玩家负")
    elif player_number == 2 and computer_number == 3:
        print("玩家出剪刀", player_number, ", 电脑出布", computer_number, "玩家胜")
    elif player_number == 3 and computer_number == 1:
        print("玩家出布", player_number, ", 电脑出拳头", computer_number, "玩家胜")
    elif player_number == 3 and computer_number == 2:
        print("玩家出布", player_number, ", 电脑出剪刀", computer_number, "玩家负")
    else:
        print("玩家不按套路出牌，请重来")
        continue
    continue_flag = input("是否继续： y/n: ")
print("游戏结束")
