import sys
import os

import re  # 正则
import winreg  # windows注册表
import zipfile  # 压缩解压
import requests


def get_report_by_chrome():
    # 下载chromedirver的镜像地址
    base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
    # 匹配前3位版本号的正则表达式
    version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')
    chrome_version = get_chrome_version(version_re)
    if chrome_version == "-1":
        print("未安装谷歌浏览器")
        return
    check_chrome_driver_update(base_url, chrome_version)
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    if chrome_version.find("116") != -1:
        executable_path = os.path.join(base_path, 'chromedriver_116.exe')
    elif chrome_version.find("115") != -1:
        executable_path = os.path.join(base_path, 'chromedriver_115.exe')
    else:
        executable_path = os.path.join(base_path, 'chromedriver.exe')
    return executable_path


# 通过注册表查询chrome版本
def get_chrome_version(version_re):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # 返回前3位版本号
    except WindowsError as e:
        # 没有安装chrome浏览器
        return "-1"


# 查询Chromedriver版本
def get_chrome_driver_version():
    path = os.getcwd() + os.path.sep
    outstd2 = os.popen(path + 'chromedriver --version').read()
    if not outstd2:
        outstd2 = os.popen('chromedriver --version').read()
        print("outstd2_system", outstd2)
    else:
        print("outstd2_local", outstd2)

    try:
        version = outstd2.split(' ')[1]
        version = ".".join(version.split(".")[:-1])
        return version
    except Exception as e:
        return "0.0.0"


# 检查chromedirver用不用更新
def check_chrome_driver_update(base_url, chrome_version):
    print(f'当前chrome版本: {chrome_version}')
    driver_version = get_chrome_driver_version()
    print(f'当前chromedriver版本: {driver_version}')
    if chrome_version == driver_version:
        print("版本兼容，无需更新.")
        return
    print("chromedriver版本与chrome浏览器不兼容，更新中>>>")
    try:
        get_latest_chrome_driver(chrome_version, base_url)
        print("chromedriver更新成功!")
    except requests.exceptions.Timeout:
        print("chromedriver下载失败，请检查网络后重试！")
    except Exception as e:
        print(f"chromedriver未知原因更新失败: {e}")


# 获取该chrome版本的最新driver版本号
def get_latest_chrome_driver(version, base_url):
    if str(version).find("116") != -1 or version.find("115") != -1:
        return
    else:
        print(version)
        url = f"{base_url}LATEST_RELEASE_{version}"
        latest_version = requests.get(url).text
        print(f"与当前chrome匹配的最新chromedriver版本为: {latest_version}")
        # 下载chromedriver
        print("开始下载chromedriver...")
        download_url = f"{base_url}{latest_version}/chromedriver_win32.zip"
        # print(download_url)
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


