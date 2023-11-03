import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import kurtosis, skew
import math
import random
import matplotlib.pyplot as plt

# 获取2010-2020 S&P500和META的数据
data_sp500 = yf.download('金科股份', start='2020-01-01', end='2020-12-31', timeout=50)
data_meta = yf.download('META', start='2020-01-01', end='2020-12-31', timeout=50)

# 数据预处理，比如合并数据等
# ...

# 蒙特卡洛模拟预测2021年的股价
simulated_prices = []
for i in range(len(data_sp500)):
    # 随机生成涨跌幅度
    move = np.random.normal(1, 0.05)  # 正态分布随机数，平均值为1，标准差为0.05
    simulated_price = data_sp500['Close'][i] * move
    simulated_prices.append(simulated_price)

simulated_prices = pd.Series(simulated_prices)

# 使用线性回归模型进行拟合分析
X = data_sp500[['Close']].values
y = data_meta['Close'].values
model = LinearRegression().fit(X, y)
mse = mean_squared_error(y, model.predict(X))  # 均方误差 MSE (Mean Squared Error)越小越好
r2 = r2_score(y, model.predict(X))  # R^2 (Coefficient of Determination)越接近1越好
rmse = math.sqrt(mse)  # 均方根误差 RMSE (Root Mean Squared Error)越小越好
explained_variance = model.coef_ @ X.T @ X @ model.coef_ / (
            model.coef_ @ X.T @ y - model.intercept_)  # 解释方差 Explained Variance
kurtosis_ratio = kurtosis(explained_variance / mse)  # 峰度 Kurtosis Ratio越接近3越好
skewness_ratio = skew(explained_variance / mse)  # 偏度 Skewness Ratio越接近0越好

# 基于预测股价做期权定价并与真实期权价格比较
# ...

# 可视化输出结果
plt.figure(figsize=(12, 6))
plt.plot(data_sp500['Close'], label='S&P500')
plt.plot(data_meta['Close'], label='META')
plt.plot(simulated_prices, label='Simulated Prices')
plt.legend()
plt.show()
