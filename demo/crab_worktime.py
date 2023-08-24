import requests
import time
import datetime
import json
# import pymysql
# from lxml.html import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'
    , 'Referer': 'http://fund.eastmoney.com'
}

# # 初始化数据库连接
# connection = pymysql.connect(host='47.102.***.**', user='root', password='root', database='scrapy', port=3306, charset='utf8')
# cursor = connection.cursor()

# 程序入口, 解析基金分类
def start_requests():
    timestamp = int(time.time() * 1000)
    callback = 'jQuery18306789193760800711_' + str(timestamp)
    start_url = f'http://redmine-pa.mxnavi.com/workreports?utf8=%E2%9C%93&report_state=3&time_begin%5B%5D=2023-08-01&time_end%5B%5D=2023-08-25&commit=%E6%9F%A5%E8%AF%A2'
    response = requests.get(start_url, headers=headers)
    # 将分类返回的数据掐头去尾，格式化成json
    # result = response.text.replace(callback, '')
    print(response.text)

    # result = result[result.index("fieldset")::result.index("/fieldset")]
    # data = json.loads(result)
    # print(result)

start_requests()