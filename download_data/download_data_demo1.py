import csv
from matplotlib import pyplot as plt

filename = "eastmoney_stock_data.csv"
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, close, open_price = [], [], []
    for row in reader:
        try:
            current_date = row[0]
            current_close = float(row[2])
            current_open_price = float(row[1])
        except ValueError:
            print('missing data')
        else:
            dates.append(current_date)
            close.append(current_close)
            open_price.append(current_open_price)

# print(open_price)

fig = plt.figure(dpi=128, figsize=(60, 6))
plt.plot(dates, close, c='red', alpha=0.5)
plt.plot(dates, open_price, c='blue', alpha=0.5)
plt.fill_between(dates, open_price, close, facecolor="blue", alpha=0.1)  # 填充两条线中间区域
plt.xlabel("date", fontsize=16)
plt.ylabel("price", fontsize=16)
fig.autofmt_xdate()
plt.gcf().autofmt_xdate()
plt.tick_params(axis='both', which="major", labelsize=15)
title = "A data"
plt.title(title, fontsize=20)
plt.show()
