import csv
import json

import requests
import pandas as pd
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import kurtosis, skew
import math
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 定义请求的URL和参数
# 2021--->2022
# url = """https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery3510458022529097849_1698917639046&secid=0.000656&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&start=20210101&end=20211231&lmt=245&_=1698917639127"""
url = """https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery3510458022529097849_1698917639046&secid=0.000656&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&start=20220101&end=20221231&lmt=360&_=1698917639127"""
url = """https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery3510458022529097849_1698917639046&secid=0.002168&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&start=20220101&end=20221231&lmt=360&_=1698917639127"""

# params = {
#     'fields': 'open,close,high,low,volume',
#     'stock_code': '000656',  # S&P500和META的股票代码
#     'interval': 'month',  # 月份K线数据
#     'start_date': '20100101',  # 开始日期为2010年1月1日
#     'end_date': '20201231'  # 结束日期为2020年12月31日
# }

# """https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery3510458022529097849_1698917639046&secid=0.300533&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&start=20210101&end=20211231&lmt=245&_=1698917639127"""
# # 发送HTTP请求并获取数据
response = requests.get(url)
result = response.content.decode("utf-8").split("(")[1].split(")")[0]
# print(type(json.loads(result)['data']["klines"]))
result = json.loads(result)['data']["klines"]
data = [item.split(",") for item in result]
print(data)
#
# # 将数据保存到本地文件
# data.to_csv('eastmoney_stock_data.csv', index=False)

# features = data[['f1', 'f2', 'f3', 'f4', 'f5', 'f6']]  # 特征列取决于你想使用哪些字段进行预测，这里假设使用'f1'到'f6'作为特征列
# target = data['f7']  # 目标列，这里假设使用'f7'作为预测的目标列，也就是股价
#
# # 数据切分
# features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2,
#                                                                             random_state=42)


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats
import math
import random
from datetime import datetime, timedelta
import requests

# 获取历史股价数据
# url = "https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery3510458022529097849_1698917639046&secid=0.300533&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&start=20210101&end=20211231&lmt=360&_=1698917639127"
# response = requests.get(url)
# response = response.content.decode("utf-8").split("(")[1].split(")")[0]
# response = []
# with open("eastmoney_stock_data.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print(row[6].split(","))
#         response.append(row[6].split(","))
data = pd.DataFrame(data[1::])
data.to_csv('eastmoney_stock_data.csv', index=False)

data['date'] = pd.to_datetime(data[0])
data['open'] = pd.to_numeric(data[1])
data['high'] = pd.to_numeric(data[3])
data['low'] = pd.to_numeric(data[4])
data['close'] = pd.to_numeric(data[2])
data['volume'] = pd.to_numeric(data[6])
data = data.sort_values('date')
# print(data)

# 创建模拟股价数据
simulated_data = []
for i in range(len(data)):
    move = np.random.normal(1, 0.01)  # 正态分布随机数，平均值为1，标准差为0.05
    simulated_price = data['close'][i] * move
    # print(data['close'].iloc[i:i + 1].values[0])
    # random_walk = data['close'].iloc[i:i + 1].values[0] + random.random() * 0.01  # 随机游走模型生成模拟股价
    simulated_data.append([simulated_price])
simulated_data = pd.DataFrame(simulated_data, columns=['close'])
# 拟合回归模型
X = data[['open']].values
y = data['close'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
kurtosis = stats.kurtosis(y_test - y_pred)
skewness = stats.skew(y_test - y_pred)

# 基于回归模型预测未来股价
simulated_data['predicted'] = regressor.predict(simulated_data[['close']].values)
simulated_data['date'] = pd.date_range(start='2023-01-01', periods=len(simulated_data))
simulated_data = simulated_data.sort_values('date')
print(simulated_data)
simulated_data.to_csv("predicted_price")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# 假设你的日期数据在一个列表中
# # 设置x轴为日期
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# 整体趋势大致相同吧，但是价格不对
plt.figure(figsize=(12, 6))
plt.plot(simulated_data['date'], simulated_data['close'])
plt.gcf().autofmt_xdate()  # 美化x轴的标签
plt.show()

