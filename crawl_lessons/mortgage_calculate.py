current_money = 2831.12
current_mortgage = 1995.49
each_month_mortgage = 1840
month = 11
year = 0
current_year = 2023
print_flag = 0
for i in range(60):
    month = month + 1
    if month > 12:
        month = 1
        year = year + 1

    current_mortgage = current_mortgage - 3.01
    current_money -= current_mortgage
    if current_money < 0:
        print("this month need cash ", month, year)
        current_money += current_mortgage + each_month_mortgage
        continue
    last_money = current_money
    last_money += each_month_mortgage

    if year == 1 and month == 7:
        each_month_mortgage = 1940
    print(f"month is :{month}, year is {current_year + year}, current_mortgage = {current_mortgage}, current_money = {current_money}, last_money = {last_money}")
    current_money = last_money
    if print_flag == 0 and current_mortgage <= each_month_mortgage:
        print_flag = 1
        print(f"from {current_year + year}-{month}, after {year} years, no longer need cash")
