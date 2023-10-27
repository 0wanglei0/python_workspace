
current_money = 4985.11
current_mortgage = 1998.5
month = 10
for i in range(120):
    month = month + 1
    if month > 12:
        month = 1

    current_mortgage = current_mortgage - 3.01
    current_money -= current_mortgage
    if current_money < 0:
        print("this month need cash")
        current_money += current_mortgage + 1840
        continue
    last_money = current_money
    last_money += 1840
    print(f"month is :{month}, current_mortgage = {current_mortgage}, current_money = {current_money}, last_money = {last_money}")
    current_money = last_money
