import calendar
import os
import sys

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

import re  # 正则
import winreg  # windows注册表
import zipfile  # 压缩解压
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': "gzip, deflate",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def test_url():
    url = "http://redmine-pa.mxnavi.com/login?username=wangleic&password=Xiaoting521&login=%E7%99%BB%E5%BD%95"
    response = requests.post(url, headers=headers)
    print(response)
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)


def auto_login():
    # print(1)

    today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    print(today)
    first_day_of_month = time.strftime("%Y-%m", time.localtime(time.time()))
    first_day_of_month = first_day_of_month + "-1"
    print(first_day_of_month)
    url = "http://redmine-pa.mxnavi.com/workreports?utf8=%E2%9C%93&report_state=3&time_begin%5B%5D=" + str(
        first_day_of_month) + "&time_end%5B%5D=" + today + "&commit=%E6%9F%A5%E8%AF%A2"
    browser.get(url)

    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.NAME, "login")
    print(username)
    print(password)
    if username:
        username.send_keys(input("用户名:"))
        password.send_keys(input("密码:"))
        login_button.click()

    time.sleep(5)

    print(browser.get_cookies())
    cookie = browser.get_cookies()[0].get("value")
    headers["Cookie"] = "_redmine_session=" + cookie
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    tables = soup.find_all('tr')

    table_dic = {}
    table_headers = []
    table_values = []
    # 遍历每个table标签
    for table in tables:
        # 查找当前table下的所有子元素
        table_header = []
        table_value = []
        children = table.find_all("th", recursive=False)
        for child in children:
            text = child.getText().replace("\n", "").replace(" ", "")
            if child.getText() == "":
                continue
            table_header.append(text)
        # print(table_header)
        td_children = table.find_all("td", recursive=False)
        for td_child in td_children:
            td_text = td_child.getText().replace("\n", "").replace(" ", "")
            table_value.append(td_text)
        # print(table_value)
        if table_header:
            table_headers.append(table_header)
        if table_value:
            table_values.append(table_value)
    if table_headers == [] or table_values == []:
        return
    table_dic["header"] = table_headers[0]
    table_dic["values"] = table_values
    print_to_file(table_dic)


def print_to_file(table_dic):
    # print(table_dic)
    print_lst = [str("日期" + "\t" + "请假类型" + "\t" + "请假时间" + "\t" + "工时" + "\t" + "加班时间" + "\n")]
    fill_value = table_dic.get("values")
    workday = 0
    external_work = float(0)
    holiday_time = 0
    for item in fill_value:
        if len(item) != 13:
            continue
        if item[3] == '':
            workday += 1
            if item[2] == "事假":
                holiday_time += float(item[6])
            current_work_time = "%.2f" % (float(item[7]) + float(item[6]) - 8)
            external_work += float(current_work_time)
            print(current_work_time)
            print(external_work)
            print_lst.append(str(item[0] + "\t" + item[2] + "\t" + item[6] + "\t" + item[7] + "\t"
                                 + str(current_work_time) + "\n"))
        else:
            this_date = item[0].split("-")
            year = int(this_date[0])
            month = int(this_date[1])
            day = int(this_date[2])
            weekday = calendar.weekday(year, month, day)
            if weekday == 6 or weekday == 5:
                external_work += float(item[6])
                print_lst.append(str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[6] + "\t" + item[6]) + "\n")
            else:
                workday += 1
                external_work += float("%.2f" % (0 if float(item[6]) - 8 < 0 else float(item[6]) - 8))

                print_lst.append(
                    str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[6] + "\t" + str(
                        "%.2f" % (0 if float(item[6]) - 8 < 0 else float(item[6]) - 8))) + "\n")
    print("workday", workday)

    print("external_work ", str("%.2f" % external_work))
    print("holiday_time", holiday_time)
    holiday_hour = external_work // 20 * 8
    expect_worktime = workday * 8

    calculate_header = ["当前负荷", "已加班", "请假合计", "可串休", "剩余串休", "扣工资工时"]
    calculate_value = [str("%.3f" % float(external_work / expect_worktime + 1)),
                       str("%.2f" % external_work), holiday_time, holiday_hour,
                       str("%.2f" % (0 if holiday_hour - holiday_time < 0 else holiday_hour - holiday_time)),
                       "0" if holiday_time - holiday_hour < 0 else str("%.2f" % (holiday_time - holiday_hour))]
    with open("work_report.xlsx", "w+", encoding="utf8") as wr:
        for string in print_lst:
            wr.write(string)

        wr.write("\n")
        wr.write("\n")
        wr.write("\n")
        for header in calculate_header:
            wr.write(header + "\t")
        wr.write("\n")

        for value in calculate_value:
            wr.write(str(value) + "\t")
        wr.write("\n")

# 通过注册表查询chrome版本
def getChromeVersion():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # 返回前3位版本号
    except WindowsError as e:
        # 没有安装chrome浏览器
        return "1.1.1"


# 查询Chromedriver版本
def getChromeDriverVersion():
    outstd2 = os.popen('chromedriver --version').read()
    try:
        version = outstd2.split(' ')[1]
        version = ".".join(version.split(".")[:-1])
        return version
    except Exception as e:
        return "0.0.0"


# 检查chromedirver用不用更新
def checkChromeDriverUpdate():
    chrome_version = getChromeVersion()
    print(f'当前chrome版本: {chrome_version}')
    driver_version = getChromeDriverVersion()
    print(f'当前chromedriver版本: {driver_version}')
    # if chrome_version == driver_version:
    #     print("版本兼容，无需更新.")
    #     return
    print("chromedriver版本与chrome浏览器不兼容，更新中>>>")
    try:
        getLatestChromeDriver(chrome_version)
        print("chromedriver更新成功!")
    except requests.exceptions.Timeout:
        print("chromedriver下载失败，请检查网络后重试！")
    except Exception as e:
        print(f"chromedriver未知原因更新失败: {e}")


# 获取该chrome版本的最新driver版本号
def getLatestChromeDriver(version):
    if str(version).find("116") != -1 or version.find("115") != -1:
        download_url = "https://registry.npmmirror.com/-/binary/chromedriver/114.0.5735.90/chromedriver_win32.zip"
        print(f"与当前chrome匹配的最新chromedriver版本为: 116.0.5845.96")
    else:
        url = f"{base_url}LATEST_RELEASE_{version}"
        latest_version = requests.get(url).text
        print(f"与当前chrome匹配的最新chromedriver版本为: {latest_version}")
        # 下载chromedriver
        print("开始下载chromedriver...")
        download_url = f"{base_url}{latest_version}/chromedriver_win32.zip"
    # 下载chromedriver
    print("开始下载chromedriver...")
    file = requests.get(download_url)
    with open("chromedriver.zip", 'wb') as zip_file:  # 保存文件到脚本所在目录
        zip_file.write(file.content)
    print("下载完成.")
    # 解压
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    print("解压完成.")


if __name__ == '__main__':
    # 下载chromedirver的镜像地址
    base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
    # 匹配前3位版本号的正则表达式
    version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')
    checkChromeDriverUpdate()
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    executable_path = os.path.join(base_path, 'ChromeDriver.exe')
    browser = webdriver.Chrome(service=Service(executable_path=executable_path))
    auto_login()
    browser.quit()
    quit()

# test_url()