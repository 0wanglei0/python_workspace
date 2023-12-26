import datetime as dt
import getpass
import sys
import time
import warnings
import os

import numpy as np
import pandas as pd
from chinese_calendar import is_workday
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re  # 正则
import winreg  # windows注册表
import zipfile  # 压缩解压
import requests

warnings.filterwarnings("ignore")
user_name = ""
pass_word = ""

# authors：cikai


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
    if chrome_version == driver_version:
        print("版本兼容，无需更新.")
        return
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

def get_data():
    df = pd.DataFrame(columns=["日期", "时长"])
    url = "http://redmine-pa.mxnavi.com"
    # driver = webdriver.Chrome()  # 打开谷歌浏览器
    option = webdriver.ChromeOptions()
    option.add_argument("headless")

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    executable_path = os.path.join(base_path, 'ChromeDriver.exe')
    # driver = webdriver.Chrome(options=option, service=Service(executable_path=executable_path))
    driver = webdriver.Chrome(service=Service(executable_path=executable_path))

    driver.maximize_window()
    driver.get(url)  # 输入网址
    driver.set_page_load_timeout(13)

    time.sleep( 5)
    driver.find_element(By.ID, "username").send_keys(user_name)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "password").send_keys(pass_word)
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "login").click()
    # driver.refresh()
    # driver.implicitly_wait(5)
    # driver.find_element(By.LINK_TEXT, "日报相关").click()
    driver.get('http://redmine-pa.mxnavi.com/workreports/')
    driver.implicitly_wait(5)
    driver.find_element(By.LINK_TEXT, "日报缺失查询").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "select_End_Time_").send_keys(str(dt.datetime.now().date()))
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "commit").click()
    driver.implicitly_wait(5)
    current_url = driver.current_url
    c_year = str(dt.datetime.now().year)[2:]
    c_month = dt.datetime.now().month
    c_day = dt.datetime.now().day
    for i in np.arange(c_day - 1):
        cal_day = i + 1
        cal_date = "{0}-{1}-{2}".format(c_year, c_month, cal_day)
        query_url = re.sub(r'\d{4}-\d{2}-\d{2}', cal_date, current_url)
        driver.get(query_url)
        driver.implicitly_wait(5)

        his_date = driver.find_element(By.XPATH, "//table[@id='workreportlost-table']/thead/tr/th[16]").text
        driver.implicitly_wait(5)

        his_hour = driver.find_element(By.XPATH, "//table[@id='workreportlost-table']/tbody/tr/td[16]").text
        driver.implicitly_wait(5)

        print(his_date, his_hour)
        df = df.append({"日期": his_date, "时长": his_hour}, ignore_index=True)
    driver.quit()
    return df


def run():
    df = get_data()
    # print(df)
    total = []
    for r in df.itertuples():
        work_date = dt.datetime.strptime(getattr(r, "日期"), "%Y-%m-%d")
        work_hour = np.float64(getattr(r, "时长"))
        if is_workday(work_date):
            if work_hour <= 0.01:
                print("工作日忘记写日报，日期=>{0}".format(work_date))
            else:
                work_hour = work_hour - 8

        total.append(work_hour)
    append_hours = np.sum(total)
    print("本月加班总时长{0}".format(round(append_hours, 2)))

def show_password(prompt):
    password = ""
    while True:
        char = getpass.getpass(prompt=prompt, stream=None)
        if char == "\r":
            break
        password += char
        prompt = "*" * len(password) + "\r"
    return password


if __name__ == '__main__':
    # base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
    # # 匹配前3位版本号的正则表达式
    # version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')
    # checkChromeDriverUpdate()
    # run()
    password = ""
    while True:
        char = getpass.getpass(prompt="请输入密码：", stream=None)
        if char == "\r":
            break
        password += char
        sys.stdout.write("*")
    print("\n您输入的密码是：", password)

