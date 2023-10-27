import csv
from matplotlib import pyplot as plt
import datetime

with open("demo_data.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(int(row[1]))
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
plt.title("Daily high temperature", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16)
plt.show()

date = datetime.datetime.strptime("2023-10-23", "%Y-%m-%d")
print(date)
"""
方法strptime() 可接受各种实参，并根据它们来决定如何解读日期。表16-1列出了其中一些这样的实参。
%A 星期的名称，如Monday
%B 月份名，如January
%m 用数字表示的月份（01~12）
%d 用数字表示月份中的一天（01~31）
%Y 四位的年份，如2015
%y 两位的年份，如15
%H 24小时制的小时数（00~23）
%I 12小时制的小时数（01~12）
%p am或pm
%M 分钟数（00~59）
%S 秒数（00~61）
"""