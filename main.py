# -*- coding:utf-8 -*-
import json
import re

import requests
import bs4
import datetime


def get_web(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59",
        "Referer": "https://weathernew.pae.baidu.com/"}
    res = requests.get(url, headers=header, timeout=5)
    content = res.text.encode('utf-8')
    return content


def parse_content(content):
    soup = bs4.BeautifulSoup(content, 'lxml')
    """
    #compile中的正则
        1."var indData ="表示我们需要开始截取的地方
        2."(.*?)"表示中间为任意字符串
        3.";$"表示第一个；结尾的地方结束
        4."re.MULTILINE",影响^与$ 锚点匹配的位置。
          没有开关，^并且$仅在整个文本的开头和结尾处匹配。使用该开关，它们也将在换行符之前或之后匹配
        5."re.DOTALL",re.DOTALL,影响.模式可以匹配的内容。
          如果没有切换，则.匹配除换行符之外的任何字符。通过该开关，换行符也将匹配
    """

    pattern = re.compile(r"window.tplData = (.*?);$", re.MULTILINE | re.DOTALL)
    script = soup.find('script', text=pattern)

    data_str = pattern.search(script.text).group(0)
    data_str = data_str.strip('window.tplData = ')
    data_str = data_str.strip(';')

    data_json = json.loads(data_str, strict=False)
    # print(data_json)

    '''
    地区
    '''
    # list_tem = []
    # position = data_json['position']
    # for i in list(position):
    #     if i == 'city':
    #         list_tem.append("城市: " + str(position[i]))
    #         continue
    #     # if i == 'country':
    #     #     list_tem.append("国家: " + str(position[i]))
    #     #     continue
    # print("".join(list_tem))

    '''
    存放天气情况
    '''
    weather_list = data_json['weather']
    list_weather = [data_json['position']['city'] + "天气： "]

    for i in list(weather_list):
        if i == 'bodytemp_info':
            list_weather.append("体感: " + str(weather_list[i]))
            continue
        if i == 'wind_direction':
            list_weather.append(", 风向: " + str(weather_list[i]))
            continue
        # if i is 'site':
        #     list_weather.append("体感温度: " + str(weather_list[i]))
        #     continue
        if i == 'weather':
            list_weather.append(", 天气: " + str(weather_list[i]))
            continue
        if i == 'dew_temperature':
            list_weather.append(", 最低温度: " + str(weather_list[i]))
            continue
        if i == 'precipitation_type':
            list_weather.append(", 降水: " + str(weather_list[i]))
            continue
        # if i is 'wind_direction_num':
        #     list_weather.append("风向: " + str(weather_list[i]))
        #     continue
        if i == 'temperature':
            list_weather.append(", 当前温度: " + str(weather_list[i]))
            continue
        if i == 'wind_power':
            list_weather.append(", 风力: " + str(weather_list[i]))
            continue
        # list_weather.append(str(i) + ": " + str(weather_list[i]))
    weather = "".join(list_weather)

    # '''
    # 存放日期
    # '''
    list_day = ""
    day_list = data_json['base']
    for i in list(day_list):
        if i == 'dateShort':
            list_day = list_day + "今天是" + str(day_list[i])
            continue
        if i == 'weekday':
            weekday = datetime.date(year, month, today.day).weekday()
            print(weekday)
            list_day = list_day + "， " + week_list[weekday]
            continue
        if i == 'lunar':
            list_day = list_day + "， 农历" + str(day_list[i])
            continue
    # 'position': {'city': '沈阳', 'country': '中国'}, 'ps_pm25': {'level': '良', 'ps_pm25': '72'}, 'feature': {
    #     'humidity': '63.0', 'wind': '东北风2级', 'sunriseTime': '06:45', 'sunsetTime': '16:21',
    #     'ultraviolet': '强'}, 'base': {'dateShort': '11月23日', 'date': '2022-11-23', 'weekday': '周四',
    #                                    'lunar': '十月三十'}
    day = "".join(list_day)
    # for each in day_list:
    #     if i <= 6:
    #         list_day.append(each.text.strip())
    #         i += 1
    # print(list_day)
    #
    # '''
    # 存放温度：最高温度和最低温度
    # '''
    # tem_list = soup.find_all('p', class_='tem')
    # i = 0
    # list_tem = []
    # for each in tem_list:
    #     if i == 0:
    #         list_tem.append(each.i.text)
    #         i += 1
    #     elif i > 0:
    #         list_tem.append([each.span.text, each.i.text])
    #         i += 1
    # print(list_tem)
    #
    # '''
    # 存放风力
    # '''
    list_wind = []
    wind_list = soup.find_all('#sfr-app > div > div.rt-body > div > div.weather-main > div > div.weather-banner > div.weather-banner-header > p.weather-banner-header-left > span:nth-child(2) > span:nth-child(2)')
    # for each in wind_list:
    #     list_wind.append(each.i.text.strip())
    print(wind_list)
    return day, weather, list_wind


def get_content(url):
    print("start")
    content = get_web(url)
    day, weather, wind = parse_content(content)
    item = 0
    print(day)
    print(weather)
    # print(tem)
    # print(wind)

    # for i in range(0, 7):
    #     if item == 0:
    #         print(day[i] + ':\t')
    #         print(weather[i] + '\t')
    #         print("今日气温：" + tem[i] + '\t')
    #         print("风力：" + wind[i] + '\t')
    #         print('\n')
    #         item += 1
    #     elif item > 0:
    #         print(day[i] + ':\t')
    #         print(weather[i] + '\t')
    #         print("最高气温：" + tem[i][0] + '\t')
    #         print("最低气温：" + tem[i][1] + '\t')
    #         print("风力：" + wind[i] + '\t')
    #         print('\n')


week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
today = datetime.datetime.today()
year, month, day_now = today.year, today.month, today.day

get_content(
    f"https://weathernew.pae.baidu.com/weathernew/pc?query=%E8%BE%BD%E5%AE%81%E6%B2%88%E9%98%B3%E5%A4%A9%E6%B0%94&srcid=4982")

