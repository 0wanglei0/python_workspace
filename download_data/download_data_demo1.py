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
        close.append(float(row[2]))
        dates.append(row[0])
        open_price.append(float(row[1]))

print(open_price)
fig = plt.figure(dpi=128, figsize=(60, 6))
plt.plot(dates, close, c='red')
plt.plot(dates, open_price, c='blue')
plt.xlabel("date", fontsize=16)
plt.ylabel("price", fontsize=16)
fig.autofmt_xdate()
plt.gcf().autofmt_xdate()
plt.tick_params(axis='both', which="major", labelsize=15)
plt.show()
