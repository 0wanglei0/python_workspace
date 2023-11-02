import requests
import pandas as pd

# 定义请求的URL和参数
url = """https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery3510458022529097849_1698917639046&secid=0.300533&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&start=20210101&end=20211231&lmt=245&_=1698917639127"""

# params = {
#     'fields': 'open,close,high,low,volume',
#     'stock_code': '000656',  # S&P500和META的股票代码
#     'interval': 'month',  # 月份K线数据
#     'start_date': '20100101',  # 开始日期为2010年1月1日
#     'end_date': '20201231'  # 结束日期为2020年12月31日
# }

"""https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery3510458022529097849_1698917639046&secid=0.300533&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&start=20210101&end=20211231&lmt=245&_=1698917639127"""
# 发送HTTP请求并获取数据
response = requests.get(url)
print(response.content.decode("utf-8"))
data = pd.DataFrame(tuple(response.content.decode("utf-8"))[0]['data'])

# 将数据保存到本地文件
data.to_csv('eastmoney_stock_data.csv', index=False)
