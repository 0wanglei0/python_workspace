for i in range(0, 3):
    for j in range(0, 4):
        print("*", end="")
    print()
print()

#正三角形
for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end="")
    print()

print()

# 倒三角
for i in range(0, 5):
    for j in range(0, 5 - i):
        print("*", end="")
    print()

print()

# 等腰三角形
"""
&&&*      n=1
&&***     n=2
&*****    n=3
*******   n=4
&是一个倒三角，*是每行输出2*n-1个

"""
m = 4
for i in range(1, m):
    for j in range(1, m - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
print()

#菱形
n = eval(input("输入行数："))
top_row = (n + 1) // 2
for i in range(1, top_row + 1):
    for j in range(1, top_row - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

bottom_row = n // 2
for i in range(1, bottom_row + 1):
    for j in range(1, i + 1):
        print(" ", end="")
    for k in range(1, 2 * (bottom_row - i + 1)):
        print("*", end="")
    print()
print()

#空心菱形  只需要输出实心菱形的第一个和最后一个*就是空心菱形了
n = eval(input("输入行数："))
while n % 2 == 0:
    n = eval(input("please re input"))

top_row = (n + 1) // 2
for i in range(1, top_row + 1):
    for j in range(1, top_row - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

bottom_row = n // 2
for i in range(1, bottom_row + 1):
    for j in range(1, i + 1):
        print(" ", end="")
    for k in range(1, 2 * (bottom_row - i + 1)):
        if k == 1 or k == 2 * (bottom_row - i + 1) - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()
