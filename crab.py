import requests
import time
import datetime
import json
import pymysql
from lxml.html import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'
    , 'Referer': 'http://fund.eastmoney.com'
}

# 初始化数据库连接
connection = pymysql.connect(host='47.102.***.**', user='root', password='root', database='scrapy', port=3306, charset='utf8')
cursor = connection.cursor()

# 程序入口, 解析基金分类
def start_requests():
    timestamp = int(time.time() * 1000)
    callback = 'jQuery18306789193760800711_' + str(timestamp)
    start_url = f'http://fundtest.eastmoney.com/dataapi1015/ztjj//GetBKListByBKType?callback={callback}&_={timestamp}'
    response = requests.get(start_url, headers=headers)
    # 将分类返回的数据掐头去尾，格式化成json
    result = response.text.replace(callback, '')
    result = result[1: result.rfind(')')]
    data = json.loads(result)
    # 遍历行业分类数据，获取名称和代号
    for item in data['Data']['hy'] :
        time.sleep(3)
        code = item['BKCode']
        category = item['BKName']
        print(code, category)
        parseFundList(code, category)
    # 遍历概念分类数据
    for item in data['Data']['gn']:
        time.sleep(3)
        code = item['BKCode']
        category = item['BKName']
        print(code, category)
        parseFundList(code, category)

# 解析每个分类下的基金列表
def parseFundList(code, category):
    timestamp = int(time.time() * 1000)
    callback = 'jQuery1830316287740290561061_' + str(timestamp)
    index = 1
    url = f'http://fundtest.eastmoney.com/dataapi1015/ztjj/GetBKRelTopicFund?callback={callback}&sort=SON_1N&sorttype=DESC&pageindex={index}&pagesize=10&tp={code}&isbuy=1&_={timestamp}'
    response = requests.get(url, headers=headers)
    result = response.text.replace(callback, '')
    result = result[1: result.rfind(')')]
    data = json.loads(result)
    totalCount = data['TotalCount']
    # 先根据totalCount计算出总页数
    pages = int(int(totalCount) / 10) + 1
    # 解析出每页基金的FCode
    for index in range(1, pages + 1):
        timestamp = int(time.time() * 1000)
        callback = 'jQuery1830316287740290561061_' + str(timestamp)
        url = f'http://fundtest.eastmoney.com/dataapi1015/ztjj/GetBKRelTopicFund?callback={callback}&sort=SON_1N&sorttype=DESC&pageindex={index}&pagesize=10&tp={code}&isbuy=1&_={timestamp}'
        response = requests.get(url, headers=headers)
        result = response.text.replace(callback, '')
        result = result[1: result.rfind(')')]
        data = json.loads(result)
        for item in data['Data']:
            time.sleep(3)
            fundCode = item['FCODE']
            fundName = item['SHORTNAME']
            parse_info(fundCode, fundName, category)


def parse_info(fundCode, fundName, category):
    url = f'http://fund.eastmoney.com/{fundCode}.html'
    response = requests.get(url, headers=headers)
    content = response.text.encode('ISO-8859-1').decode('UTF-8')
    html = etree.HTML(content)
    worth = html.xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[1]/dl[2]/dd[1]/span[1]/text()')
    if worth:
        worth = worth[0]
    else:
        worth = 0
    scope = html.xpath('//div[@class="infoOfFund"]/table/tr[1]/td[2]/text()')[0].replace('：', '')
    manager = html.xpath('//div[@class="infoOfFund"]/table/tr[1]/td[3]/a/text()')[0]
    create_time = html.xpath('//div[@class="infoOfFund"]/table/tr[2]/td[1]/text()')[0].replace('：', '')
    company = html.xpath('//div[@class="infoOfFund"]/table/tr[2]/td[2]/a/text()')[0]
    level = html.xpath('//div[@class="infoOfFund"]/table/tr[2]/td[3]/div/text()')
    if level:
        level = level[0]
    else:
        level = '暂无评级'
    month_1 = html.xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()')
    month_3 = html.xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[1]/dl[2]/dd[2]/span[2]/text()')
    month_6 = html.xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[1]/dl[3]/dd[2]/span[2]/text()')
    if month_1:
        month_1 = month_1[0]
    else:
        month_1 = ''

    if month_3:
        month_3 = month_3[0]
    else:
        month_3 = ''

    if month_6:
        month_6 = month_6[0]
    else:
        month_6 = ''
    print(fundName, fundCode, category, worth, scope, manager, create_time, company, level, month_1, month_3, month_6, sep='|')
    # 存储到mysql
    today = datetime.date.today()
    sql = f"insert into fund_info values('{today}', '{fundName}', '{fundCode}', '{category}', '{worth}', '{scope}', '{manager}', '{create_time}', '{company}', '{level}', '{month_1}', '{month_3}', '{month_6}')"
    cursor.execute(sql)
    connection.commit()
# 开始爬取
start_requests()