import requests
from lxml import etree
import csv

def get_weather(url):
    weather_info = []
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    resp = requests.get(url, headers=header)
    resp_html = etree.HTML(resp.text)
    resp_list = resp_html.xpath("//ul[@class='thrui']/li")
    # print(resp_list)
    for li in resp_list:
        # print(li)
        day_weather_info = {"date_time": li.xpath("./div[1]/text()")[0].split(" ")[0]}
        high = li.xpath("./div[2]/text()")[0]
        day_weather_info["high"] = high[:high.find("℃")]

        low = li.xpath("./div[3]/text()")[0]
        day_weather_info["low"] = low[:low.find("℃")]

        day_weather_info["weather"] = li.xpath("./div[4]/text()")[0]
        weather_info.append(day_weather_info)
    return weather_info


weathers = []

for month in range(1, 12):
    weather_time = '2023' + ("0" + str(month) if month < 10 else str(month))
    # print(weather_time)

    url = f"https://lishi.tianqi.com/shenyang/{weather_time}.html"
    weather = get_weather(url)
    weathers.append(weather)

# print(weathers)

with open("weather.csv", "w", encoding="GBK", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["日期", "最高温", "最低温", "天气"])
    # print(weathers)

    writer.writerows([list(day_weather_dict.values()) for month_weather in weathers for day_weather_dict in month_weather])
