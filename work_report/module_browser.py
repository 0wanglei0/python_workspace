import os

from webdriver_manager.chrome import ChromeDriverManager

import module_weekdays as weekdays
import time
import stdiomask
from selenium.webdriver.common.by import By
import module_crypto as crypto
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import platform
import judge_browsers as judge
# import chrome_driver_update as cdu
from work_report import utils

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
    log.info('MicrosoftEdge' in os.getenv('PATH'))
    log.info(judge.init_edge())
    if get_current_system() == "Windows" and judge.init_edge():
        # 如果这里出现SSL异常，可能是应为开了代理导致SSL验证不过
        this_browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        log.info_out("使用Edge")

    if this_browser is None:
        # this_browser = webdriver.Chrome(service=Service(executable_path=cdu.get_report_by_chrome()))
        this_browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
    days = weekdays.get_start_end_days_string_by_month(year_month)
    log.d("days", days)
    url = "https://redmine-pa.mxnavi.com/workreports?utf8=%E2%9C%93&report_state=3&time_begin%5B%5D=" + \
          days[0] + "&time_end%5B%5D=" + days[1] + "&commit=%E6%9F%A5%E8%AF%A2"
    local_browser.get(url)

    time.sleep(2)
    empty_user_info = True
    # print(username)
    # print(password)
    with open("user_info.txt", "a+", encoding="utf8") as user_info:
        user_info.seek(0)
        lines = user_info.readlines()
        while True:
            username_element = local_browser.find_element(By.ID, "username")
            username_element.clear()
            password_element = local_browser.find_element(By.ID, "password")
            login_button = local_browser.find_element(By.NAME, "login")
            if not lines:
                empty_user_info = True
                username = input("请输入用户名:")
                password = stdiomask.getpass(prompt='password: ', mask='*')
                encrypt_pass = crypto.aes_encrypt(password)
            else:
                empty_user_info = False
                log.info_out("正在自动登录,请稍后...")
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
                time.sleep(1)
                try:
                    login_error = local_browser.find_element(By.ID, "flash_error")
                    if login_error:
                        log.info_out("用户名或密码错误，请重新输入")
                        continue
                except Exception as e:
                    log.info(e)

                if empty_user_info:
                    log.save_to_file(username, user_info)
                    log.save_to_file(encrypt_pass, user_info)
                break
            else:
                raise Exception("browser is not load right, please retry")

    log.info_out("登录成功")

    time.sleep(1)
    set_cookie(local_browser)
    # goto_workreport(local_browser, days)
    return [local_browser, url]


def set_cookie(local_browser):
    cookie = local_browser.get_cookies()[0].get("value")
    headers["Cookie"] = "_redmine_session=" + cookie


def goto_workreport(local_browser, days):
    utils.use_js_change_value(local_browser, "time_begin_", days[0])
    utils.use_js_change_value(local_browser, "time_end_", days[1])
    time.sleep(10)
    commit_button = local_browser.find_element(By.NAME, "commit")
    commit_button.click()
    time.sleep(1)