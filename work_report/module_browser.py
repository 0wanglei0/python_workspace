import module_weekdays as weekdays
import getpass
import time
from selenium.webdriver.common.by import By
import module_crypto as crypto
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import platform
import judge_browsers as judge
import chrome_driver_update as cdu


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': "gzip, deflate",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def get_current_system():
    return platform.system()


def get_current_default_browser(log):
    log.info_out("浏览器加载中，请稍后...")

    this_browser = None
    if get_current_system() == "Windows" and judge.init_edge():
        # 如果这里出现SSL异常，可能是应为开了代理导致SSL验证不过
        this_browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        log.info_out("使用Edge")

    if this_browser is None:
        this_browser = webdriver.Chrome(service=Service(executable_path=cdu.get_report_by_chrome()))
        log.info_out("使用Chrome")

    if this_browser is None:
        log.info_out("没有找到合适的浏览器")
        return None

    return this_browser


def auto_login(log, year_month):
    local_browser = get_current_default_browser(log)
    if local_browser is None:
        return None

    log.info_out("浏览器启动完成！")
    log.info_out("正在自动登录,请稍后...")
    days = weekdays.get_start_end_days_string_by_month(year_month)
    log.d("days", days)
    url = "http://redmine-pa.mxnavi.com/workreports?utf8=%E2%9C%93&report_state=3&time_begin%5B%5D=" + \
          days[0] + "&time_end%5B%5D=" + days[1] + "&commit=%E6%9F%A5%E8%AF%A2"
    local_browser.get(url)

    time.sleep(3)
    username_element = local_browser.find_element(By.ID, "username")
    password_element = local_browser.find_element(By.ID, "password")
    login_button = local_browser.find_element(By.NAME, "login")
    # print(username)
    # print(password)
    with open("user_info.txt", "a+", encoding="utf8") as user_info:
        user_info.seek(0)
        lines = user_info.readlines()
        if not lines:
            username = input("用户名:")
            password = getpass.getpass("password:")
            encrypt_pass = crypto.aes_encrypt(password)
            log.save_to_file(username, user_info)
            log.save_to_file(encrypt_pass, user_info)
        else:
            username = lines[0].replace("\n", "")
            password = lines[1].replace("\n", "")
            password = crypto.aes_decrypt(password)
            # print(username)
            # print(password)

    if username_element:
        username_element.send_keys(username)
        time.sleep(1)
        password_element.send_keys(password)
        time.sleep(1)
        login_button.click()
    else:
        raise Exception("browser is not load right, please retry")

    log.info_out("登录成功")

    time.sleep(1)
    set_cookie(local_browser)
    return [local_browser, url]


def set_cookie(local_browser):
    cookie = local_browser.get_cookies()[0].get("value")
    headers["Cookie"] = "_redmine_session=" + cookie
