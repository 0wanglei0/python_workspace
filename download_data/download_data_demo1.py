import csv
from matplotlib import pyplot as plt

filename = "eastmoney_stock_data.csv"
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, close = [], []
    for row in reader:
        close.append(float(row[2]))
        dates.append(row[0])
    print(close)

fig = plt.figure(dpi=128, figsize=(60, 6))
plt.plot(dates, close, c='red')
plt.xlabel("date", fontsize=16)
plt.ylabel("Close", fontsize=16)
fig.autofmt_xdate()
plt.gcf().autofmt_xdate()
plt.tick_params(axis='both', which="major", labelsize=15)
plt.show()
