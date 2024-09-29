# 公积金


import datetime

current_money = 3810.57
each_month_mortgage = 1940

today = datetime.datetime.today()
month = 7
year = 0
current_year = 2024
print_flag = 0

# current_mortgage = 1971.38
# benji_month = 1166.67
# benji_total = 310333.02
# each_reduce = 3.01
# last_money = 0

# 第一次还3W 2025 20年
# current_mortgage = 1856.25
# benji_month = 1125
# benji_total = 270000
# each_reduce = 3.05
# last_money = 5176

# 第二次还3W 2026 15年
# current_mortgage = 1818.06
# benji_month = 1222.22
# benji_total = 230000
# each_reduce = 3.31
# last_money = 5176

# 第3次还3W 2027 10年
# current_mortgage = 1987.50
# benji_month = 1500
# benji_total = 180000
# each_reduce = 4.06
# last_money = 5697


# 第4次还3W 2028 10年
# current_mortgage = 1435.42
# benji_month = 1083.33
# benji_total = 130000
# each_reduce = 2.93
# last_money = 3564

# 第4次还3W 2029 5年
# current_mortgage = 1646.88
# benji_month = 1416.67
# benji_total = 85000
# each_reduce = 3.84
# last_money = 10636

# 第4次还3W 2030 2年
current_mortgage = 1553.13
benji_month = 1458.33
benji_total = 35000
each_reduce = 3.95
last_money = 7970

for i in range(13):
    if benji_total <= last_money:
        print(f"在 month is :{month}, year is {current_year + year} 可以一次还了 {benji_total} ")
        break
    if i == 360 - 94 - 1:
        print(f"{i} 还完了 {str(current_mortgage)}")
        break
    month = month + 1
    if month > 12:
        month = 1
        year = year + 1
        # 提前还款简单算法，每次还款会重新计算
        if benji_total - 30000 > 0:
            benji_total = benji_total - 30000
            print("每年多还30000")
        else:
            print(f"在 month is :{month}, year is {current_year + year},取出公积金{last_money}, 可以一次还了 {benji_total} ")
            break
        # print(benji_total)

    current_mortgage = current_mortgage - each_reduce
    current_money -= current_mortgage
    if current_money < 0:
        print(f"this month need cash , {month}, {year+current_year}, {current_mortgage}")
        current_money += current_mortgage + each_month_mortgage
        continue
    last_money = current_money
    last_money += each_month_mortgage
    benji_total = benji_total - benji_month
    # each_month_mortgage = 1940
    # if year == 1 and month == 7:
    #     each_month_mortgage = 1840
    print(f"month is :{month}, year is {current_year + year}, current_mortgage = {current_mortgage},"
          f" current_money = {current_money}, last_money = {last_money}, benjin_total = {benji_total}")
    current_money = last_money
    if print_flag == 0 and current_mortgage <= each_month_mortgage:
        print_flag = 1
        print(f"from {current_year + year}-{month}, after {year} years, no longer need cash")
