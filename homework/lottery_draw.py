import random

rewards = ["泰国5日游+手术费报销", "iPhone14手机", "三斤苹果"]
person_num = {"1等奖": 3, "2等奖": 6, "3等奖": 30}

employees = []
for employee in range(1, 301):
    employees.append(f"员工{employee}")
# print(employees)

print("now, let's begin")
print("========================")

for i in range(3, 0, -1):
    level = f"{i}等奖"
    print(f"开始抽{i}等奖")
    nums = person_num.get(level, 0)
    win_list = []
    for num in range(nums):
        number = random.randint(1, len(employees))
        win_person = f"员工{number}"
        win_list.append(win_person)
        employees.pop(number)

    print(f"恭喜以下员工{win_list} \n获得奖励：{rewards[i - 1]}")
    print()
    print()