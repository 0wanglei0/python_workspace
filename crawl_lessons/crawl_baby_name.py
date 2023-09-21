"""
宝宝姓名批量打分程序

·思路：准备名字集合，使用爬虫程序批量打分，供起名参考
·爬取网站：http://life.httpcn.com.xingming.asp
`github代码地址：https://github.com/peiss/chinese-name-score
`特点：表单提取的爬取
·网站编码GB2312

参数中中文乱码可以去百度url编码解码的网站进行解析
"""
from urllib.parse import urlencode

import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import execjs

url = "https://life.httpcn.com/xingming.asp"

params = {
    "isbz": 1,
    "xing": "王".encode("gb2312"),  # 王
    "ming": "磊".encode("gb2312"),  # 磊
    "sex": 1,
    "data_type": 1,
    "year": "1992",
    "month": "10",
    "day": "9",
    "hour": "4",
    "minute": "10",
    "pid": "辽宁".encode("gb2312"),  # 辽宁.encode("gb2312")
    "cid": "沈阳".encode("gb2312"),
    "wxxy": 0,
    "xishen": "金".encode("gb2312"),
    "yongshen": "金".encode("gb2312"),
    "check_agree": "agree",
    "act": "submit"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

select_date_js = """
    function set_year() {
        var tmp = "<option value=\"" +  + "\" selected>" + i + "</option>";
        document.writeln(tmp);
    }
"""
# 发送 GET 请求并获取响应
# response = requests.get(url)
session = HTMLSession()
resp = session.get(url)
resp.html.render()
select = resp.html.find('select#year')
print(select)
# 解析 HTML 并找到 select 元素
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# execjs.compile(select_date_js)
#
# year_select_element = soup.find('select', {'id': 'year'})
# elements = year_select_element.contents
# elements[1] = """
# <option value="2023" selected>2023</option>"
# """
# print(elements)
# month_select_element = soup.find('select', {'id': 'month'})
# month_elements = month_select_element.contents
# month_elements[1] = """
# <option value="12" selected>12</option>"
# """
# print(month_elements)
# day_select_element = soup.find('select', {'id': 'day'})
# day_elements = day_select_element.contents
# day_elements[1] = """
# <option value="12" selected>12</option>"
# """
# print(elements)


# month_select_element = soup.find('select', {'id': 'month'})
# day_select_element = soup.find('select', {'id': 'day'})
#
# # 找到要选择的选项并模拟选择操作
# # year_select_element = year_select_element.find('option', {'value': '1992'})
# print(year_select_element)
# # year_select_element['selected'] = "True"
# month_select_element = month_select_element.find('option', {'value': '1992'})
# # month_select_element['selected'] = "True"
# day_select_element = day_select_element.find('option', {'value': '1992'})
# day_select_element['selected'] = "True"

# 获取选择后的结果并打印
# selected_options = [option['value'] for option in year_select_element.find_all('option', {'selected': True})]
# print(selected_options)
# selected_options = [option['value'] for option in month_select_element.find_all('option', {'selected': True})]
# print(selected_options)
# selected_options = [option['value'] for option in day_select_element.find_all('option', {'selected': True})]
# print(selected_options)

# resp = requests.post(url, headers=headers, params=urlencode(params))
# print(resp.status_code)
# resp.encoding = "gb2312"
# print(resp.text)

# soup = BeautifulSoup(resp.text, "html.parser")
# print(soup)
# divs = soup.find_all("div")
# for div in divs:
#     if "姓名五格评分" not in div.get_text():
#         continue
#     print(div)


