import requests
import pandas as pd

# 定义请求的URL和参数
url = 'http://push2his.eastmoney.com/api/qt/stock/kline_build/get'
params = {
    'fields': 'open,close,high,low,volume',
    'stock_code': '399001,300054',  # S&P500和META的股票代码
    'interval': 'month',  # 月份K线数据
    'start_date': '20100101',  # 开始日期为2010年1月1日
    'end_date': '20201231'  # 结束日期为2020年12月31日
}

# 发送HTTP请求并获取数据
response = requests.get(url, params=params)
data = pd.DataFrame(response.json()['data'])

# 将数据保存到本地文件
data.to_csv('eastmoney_stock_data.csv', index=False)
