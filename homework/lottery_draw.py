import random

rewards = ["泰国5日游+手术费报销", "iPhone14手机", "三斤苹果"]
person_num = {"1等奖": 3, "2等奖": 6, "3等奖": 30}

employees = []
for employee in range(1, 301):
    employees.append(f"员工{employee}")
random.shuffle(employees)

# print("now, let's begin")
# print("========================")
#
# for i in range(3, 0, -1):
#     level = f"{i}等奖"
#     print(f"开始抽{i}等奖")
#     nums = person_num.get(level, 0)
#     win_list = []
#     for num in range(nums):
#         number = random.randint(1, len(employees))
#         win_person = f"员工{number}"
#         win_list.append(win_person)
#         employees.pop(number)
#
#     print(f"恭喜以下员工{win_list} \n获得奖励：{rewards[i - 1]}")
#     print()
#     print()



import tkinter as tk

# 定义一个列表，包含一些人名
# employees = ['张三', '李四', '王五', '赵六']

# 定义一个变量，用于记录当前的人名索引
current_index = 0

# 定义一个函数，用于更新人名
def update_name():
    global current_index
    # 获取当前的人名
    current_name = employees[current_index]
    # 将人名中的每个字母都变成大写
    new_name = ''.join([letter.upper() for letter in current_name])
    # 将新的人名显示在界面上
    name_label.config(text=new_name)
    # 如果当前的人名索引等于列表的长度减一，则将其设置为0
    if current_index == len(employees) - 1:
        current_index = 0
    # 否则，将当前的人名索引加1
    else:
        current_index += 1
    # 每隔0.5秒调用一次update_name函数
    root.after(50, update_name)

# 创建一个窗口
root = tk.Tk()
root.title('人名变换')

# 创建一个标签，用于显示变换后的人名
name_label = tk.Label(root, text='')
name_label.pack()

# 创建一个按钮，用于停止变换
stop_button = tk.Button(root, text='停止变换', command=root.quit)
stop_button.pack()

# 调用update_name函数，开始变换人名
update_name()

# 进入消息循环
root.mainloop()
