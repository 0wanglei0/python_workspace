"""
进制转换

"""
import random

num = eval(input("please input decimal: "))
print(num, " 的二进制数是： ", bin(num))
print(num, " 的hex进制数是： ", hex(num))
print(num, " 的8进制数是： ", oct(num))

num = random.randint(1, 100)
print("num is ", num)

dictionary = {"id": "1001", "name": "wang"}
print(dictionary["id"])
print(dictionary.get("id"))

# 97-123
for item in range(ord('A'), ord('Z')):
    print(chr(item), "的ASCII码是：", item)

for item in range(ord('a'), ord('z')):
    print(chr(item), "的ASCII码是：", item)


import math
for i in range(100, 1000):
    first = i % 10
    second = i // 10 % 10
    third = i // 100

    if math.pow(first, 3) + math.pow(second, 3) + math.pow(third, 3) == i:
        print("水仙花数：", i)


years = [82, 93, 42, 58, 29, 27, 92, 0]
for index, value in enumerate(years):
    if value == 0:
        years[index] = int(str("200") + str(0))
    else:
        years[index] = int(str("19") + str(value))

years.sort()
print(years)

# 倒序输出  开始，结束，步长
for i in range(len(years)-1, -1, -1):
    print(years[i])

print("此处不换行", "add sep", sep="-", end="", file=None)
print()

scores = (("a", 3), ("b", 3), ("c", 3), ("d", 3))
for index, item in enumerate(scores):
    for score in item:
        print(score, end="\t")
    print()


origin_string = "aasdklfjaernasdfnaasdjkfan"
input_string = input("please input string: ")
print(f"{input_string}在{origin_string}中一共出现了{origin_string.lower().count(input_string.lower())}次")

lst = ["01", "电风扇", "Media", 500]
print("000{0}\t{1}\t{2}\t￥{3:0.2f}".format(lst[0], lst[1], lst[2], lst[3]))

a = input("please input:")
try:
    if a:
        raise Exception("input error")
except Exception as e:
    print(e)

b = "#abcd#efg"
print(b.strip("#")) #去掉第一个字符
print(b.split("#")) # 分割字符串