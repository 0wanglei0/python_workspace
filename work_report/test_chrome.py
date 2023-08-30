import calendar
import platform
import sys

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import requests
import getpass

import judge_browsers as judge
import chrome_driver_update as cdu
import module_weekdays as weekdays
import module_crypto as crypto
import prettytable as ptb


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': "gzip, deflate",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def test_url_cookies():
    url = "http://redmine-pa.mxnavi.com/login?username=&password=&login=%E7%99%BB%E5%BD%95"
    response = requests.post(url, headers=headers)
    print(response)
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)


def auto_login(browser):
    days = weekdays.get_start_end_days_string()
    # print(days)
    url = "http://redmine-pa.mxnavi.com/workreports?utf8=%E2%9C%93&report_state=3&time_begin%5B%5D=" + \
        days[0] + "&time_end%5B%5D=" + days[1] + "&commit=%E6%9F%A5%E8%AF%A2"
    browser.get(url)

    time.sleep(3)
    username_element = browser.find_element(By.ID, "username")
    password_element = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.NAME, "login")
    # print(username)
    # print(password)
    with open("user_info.txt", "a+", encoding="utf8") as user_info:
        user_info.seek(0)
        lines = user_info.readlines()
        if not lines:
            username = input("用户名:")
            password = getpass.getpass("password:")
            encrypt_pass = crypto.aes_encrypt(password)
            print(username, file=user_info)
            print(encrypt_pass, file=user_info)
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

    time.sleep(5)
    cookie = browser.get_cookies()[0].get("value")
    get_work_time(cookie, url)


def get_work_time(cookie, url):
    # print(browser.get_cookies())
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
    total_time_to_file(table_dic)


def total_time_to_file(table_dic):
    # print(table_dic)
    print_lst = [str("日期" + "\t" + "请假类型" + "\t" + "请假时间" + "\t" + "工时" + "\t" + "加班时间" + "\t" + "在岗时长" + "\t" + "漏填日报" + "\n")]
    fill_value = table_dic.get("values")
    workday = 0
    external_work = float(0)
    holiday_time = 0
    for item in fill_value:
        if len(item) != 13:
            if len(item) == 10 and item[4] == '' and item[7] == '':
                if item[1] == "事假" or item[1] == "病假":
                    holiday_time += float(item[5])
                last_item = print_lst[len(print_lst) - 1].split("\t")
                current_day_total = float(item[5]) + float(last_item[3])
                current_holiday_type = item[1] if last_item[1] == "" else last_item[1]
                current_holiday_time = item[5]
                last_external_work_time = float(last_item[4])

                # print("current_holiday_time 1", current_holiday_time)
                if last_item[1] != "":
                    current_holiday_type = last_item[1] + "+" + item[1]
                    current_holiday_time = f"{last_item[2]} + {item[5]} = {float(last_item[2]) + float(item[5])}"
                    current_day_total += float(last_item[2])

                external_work = external_work - last_external_work_time + current_day_total - 8
                new_item_string = last_item[0] + "\t" + current_holiday_type + "\t" + current_holiday_time \
                                  + "\t" + last_item[3] \
                                  + "\t" + str("%.2f" % (current_day_total - 8)) \
                                  + "\t" + last_item[5] \
                                  + "\t" + str(
                    "%.2f" % (0 if 8 - float(current_day_total) < 0 else 8 - float(current_day_total)))
                print_lst[len(print_lst) - 1] = new_item_string + "\n"
                # print("last_item", new_item_string)
                # print("item", item)
            continue
        if item[5] == '':
            workday += 1
            if item[2] == "事假" or item[2] == "病假":
                holiday_time += float(item[6])
            current_external_work_time = 0 if (float(item[7]) + float(item[6]) - 8) < 0 else float(item[7]) + float(item[6]) - 8
            external_work += current_external_work_time
            # print("current_external_work_time", current_external_work_time)
            # print("external_work", external_work)
            total_work = float(item[7]) + float(item[6])
            standard_time = 0 if 8 - total_work < 0 else 8 - float(total_work)

            print_lst.append(str(item[0] + "\t" + item[2] + "\t" + item[6] + "\t" + item[7] + "\t"
                                 + str("%.2f" % current_external_work_time) + "\t"
                                 + item[8] + "\t"
                                 + str("%.2f" % standard_time) + "\n"))
        else:
            this_date = item[0].split("-")
            year = int(this_date[0])
            month = int(this_date[1])
            day = int(this_date[2])
            weekday = calendar.weekday(year, month, day)
            if weekday == 6 or weekday == 5:
                external_work += float(item[7])
                print_lst.append(str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[7] + "\t" + item[7]) + "\t" + "" + "\t" + "" + "\n")
            else:
                workday += 1
                external_work += float("%.2f" % (0 if float(item[7]) - 8 < 0 else float(item[7]) - 8))
                print_lst.append(
                    str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[7]
                        + "\t" + str("%.2f" % (0 if float(item[7]) - 8 < 0 else float(item[7]) - 8)))
                        + "\t" + item[8]
                        + "\t" + str("%.2f" % (0 if 8 - float(item[7]) < 0 else 8 - float(item[7]))) + "\n")
    print("workday", workday)

    print("external_work ", str("%.2f" % external_work))
    print("holiday_time", holiday_time)
    holiday_hour = external_work // 20 * 8
    expect_worktime = len(weekdays.get_workdays()) * 8

    calculate_header = ["当前负荷", "已加班", "请假合计", "可串休", "剩余串休", "扣工资工时"]
    calculate_value = [str("%.3f" % float(external_work / expect_worktime + 1)),
                       str("%.2f" % external_work), holiday_time, holiday_hour,
                       str("%.2f" % (0 if holiday_hour - holiday_time < 0 else holiday_hour - holiday_time)),
                       "0" if holiday_time - holiday_hour < 0 else str("%.2f" % (holiday_time - holiday_hour))]
    show_work_report(print_lst)
    show_work_report_analysis(calculate_value)
    write_to_file(print_lst, calculate_header, calculate_value)



def write_to_file(print_lst, calculate_header, calculate_value):
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

def get_current_default_browser():
    print("start")
    # print(get_current_system() == "Windows")
    # print(judge.init_edge())
    if get_current_system() == "Windows" and judge.init_edge():
        browser = webdriver.Edge()
        print("使用Edge")
    else:
        browser = webdriver.Chrome(service=Service(executable_path=cdu.get_report_by_chrome()))

    try:
        auto_login(browser)
        browser.quit()
    except Exception as e:
        log_file = open("error.log", "a+")
        print(time.strftime("%Y-%m-%d %H:%M:%S.sss", time.localtime(time.time())), e, file=log_file)
        log_file.close()

def get_current_system():
    return platform.system()


def show_work_report(work_list):
    tb = ptb.PrettyTable()
    tb.field_names = ["日期", "请假类型", "请假时间", "工时", "加班时间", "在岗时长", "漏填日报"]
    new_list = work_list[1::]
    for item in new_list:
        field_item = item.replace("\n", "").split("\t")
        print(field_item)
        lst = [field_item[0], field_item[1], field_item[2], field_item[3], field_item[4], field_item[5], field_item[6]]
        tb.add_row(lst)
    print(tb)


def show_work_report_analysis(work_total):
    tb_total = ptb.PrettyTable()
    tb_total.field_names = ["当前负荷", "已加班", "请假合计", "可串休", "剩余串休", "扣工资工时"]
    tb_total.add_row(work_total)
    print(tb_total)


# ios 运行可能要在mac上运行pyinstaler
# windows
#  ..\python_workspace\Scripts\pyinstaller.exe -F .\test_chrome.py
#  --add-binary "chromedriver.exe;." --add-binary "chromedriver_116.exe;."
#  --add-binary "chromedriver_115.exe;."
if __name__ == '__main__':
    get_current_default_browser()
    while True:
        if input("输入Enter退出") + "1":
            sys.exit()

# test_url()