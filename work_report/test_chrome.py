import calendar
import platform
import sys
import datetime
import time

import execjs
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

""" ..\python_workspace\Scripts\pyinstaller.exe - F.\test_chrome.py - -add - binary
"chromedriver.exe;." - -add - binary
"chromedriver_116.exe;." - -add - binary
"chromedriver_115.exe;.\" """
def test_url_cookies():
    url = "http://redmine-pa.mxnavi.com/login?username=&password=&login=%E7%99%BB%E5%BD%95"
    response = requests.post(url, headers=headers)
    print(response)
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)


def auto_login(local_browser):
    days = weekdays.get_start_end_days_string_by_month(year_month)
    # print(days)
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
    return [local_browser, url]

def set_cookie(local_browser):
    cookie = local_browser.get_cookies()[0].get("value")
    headers["Cookie"] = "_redmine_session=" + cookie

def get_work_time(url):
    # print(browser.get_cookies())
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
    return table_dic

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

    return [print_lst, calculate_header, calculate_value]

def write_to_file(print_lst, calculate_header, calculate_value):
    with open("work_report.xlsx", "w+", encoding="utf8") as wr:
        # wr.write(print_lst.replace(",", "\t"))
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

def calculate_loss_time(loss_work_time):
    if loss_work_time == {}:
        print("work report complete")
        return []

    _key_for_choose = []
    _keys = list(loss_work_time.keys())
    chooses = []
    # print(_keys)
    for index in range(len(_keys)):
        choose = f"{index}.{_keys[index]}"
        chooses.append(choose)
        _key_for_choose.append(_keys[index])
    return [_keys, _key_for_choose, chooses]


def log_work_time(local_browser, _keys, _key_for_choose, _chooses):
    # print("_keys", _keys)
    # print("_key_for_choose", _key_for_choose)
    # print("_chooses", _chooses)
    while True:
        print(_chooses)
        what_input = input("请选择填写日报日期序号(按q退出)：")
        if what_input == "q":
            break
        choose_index = eval(what_input)
        if choose_index < 0 or choose_index > len(_key_for_choose):
            break

        choose_key = _key_for_choose[choose_index]
        choose_value = loss_work_time_dict.get(choose_key)
        print(choose_value)
        all_issues_url = """https://redmine-pa.mxnavi.com/issues?c%5B%5D=project&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=subject&f%5B%5D=status_id&f%5B%5D=assigned_to_id&f%5B%5D=project.status&op%5Bassigned_to_id%5D=%3D&op%5Bproject.status%5D=%3D&op%5Bstatus_id%5D=o&set_filter=1&sort=priority%3Adesc%2Cupdated_on%3Adesc&v%5Bassigned_to_id%5D%5B%5D=me&v%5Bproject.status%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D="""
        local_browser.get(all_issues_url)
        time.sleep(2)
        issue_id = input("请输入要登记工时的任务id：")
        url = f"https://redmine-pa.mxnavi.com/issues/{issue_id}/time_entries/new"
        local_browser.get(url)

        date_input = local_browser.find_element(By.ID, "time_entry_spent_on")
        use_js_change_value(local_browser, "time_entry_spent_on", _keys[choose_index])
        time.sleep(1)

        work_hours_input = local_browser.find_element(By.ID, "time_entry_hours")
        comments_input = local_browser.find_element(By.ID, "time_entry_comments")
        day_logged_time_info = local_browser.find_element(By.ID, "day_logged_time")
        commit_button = local_browser.find_element(By.NAME, "commit")
        continue_button = local_browser.find_element(By.NAME, "continue")

        day_logged_time = day_logged_time_info.text
        logged_time = day_logged_time[day_logged_time.index(": ") + 2:day_logged_time.index(","):]
        total_time = day_logged_time[day_logged_time.index("间：") + 2:day_logged_time.index("(单位")]
        print(day_logged_time)

        input_work_hours = input("请输入要登记的时间(可空，填入全部在岗时间)：")
        input_work_comments = input("请输入要登记的注释（可空）：")
        if input_work_hours == "":
            residue_time = float(total_time) - float(logged_time)
            if residue_time < 0:
                print("日报已填写")
                continue
            input_work_hours = str("%.2f" % (float(total_time) - float(logged_time)))

        if date_input:
            work_hours_input.send_keys(input_work_hours)
            comments_input.send_keys(input_work_comments)
            if eval(input_work_hours) < float(total_time):
                continue_button.click()
            else:
                commit_button.click()

        time.sleep(3)
        residue_time = float(total_time) - float(logged_time) - float(input_work_hours)
        if len(key_for_choose) == 0 and residue_time == 0:
            key_for_choose.pop(choose_index)
            print("日报填写完成，结束运行")
            break
        else:
            is_goon = input("是否继续填写日报 Y/N")
            if is_goon == "Y" or is_goon == "y":
                continue
            else:
                print("日报填写完成，结束运行")
                break

def use_js_change_value(_browser, element_id, value):
    js = f"""
        element = document.getElementById("{element_id}")
        element.value = '{value}'
    """
    #
    # print(js)
    # print(value)
    _browser.execute_script(js)

def get_current_default_browser():
    print("start")
    # print(get_current_system() == "Windows")
    # print(judge.init_edge())
    if get_current_system() == "Windows" and judge.init_edge():
        this_browser = webdriver.Edge()
        print("使用Edge")
    else:
        this_browser = webdriver.Chrome(service=Service(executable_path=cdu.get_report_by_chrome()))

    return this_browser

def get_current_system():
    return platform.system()


def show_work_report(work_list, input_month):
    # print(work_list)
    tb = ptb.PrettyTable()
    tb.field_names = ["日期", "请假类型", "请假时间", "工时", "加班时间", "在岗时长", "漏填日报"]
    new_list = work_list[1::]
    work_days = weekdays.get_workdays_by_month(input_month)
    for item in new_list:
        field_item = item.replace("\n", "").split("\t")
        # print(field_item)
        lst = [field_item[0], field_item[1], field_item[2], field_item[3], field_item[4], field_item[5], field_item[6]]
        tb.add_row(lst)
        date_date = field_item[0].split("-")
        date = datetime.date(int(date_date[0]), int(date_date[1]), int(date_date[2]))
        if date in work_days:
            if field_item[6] != "" and field_item[6] != "0.00":
                loss_work_time_dict[field_item[0]] = [field_item[2], field_item[3], field_item[5]]
            work_days.pop(work_days.index(date))
    if len(work_days) != 0:
        for item in work_days:
            loss_work_time_dict[item.strftime("%Y-%m-%d")] = []
    print(loss_work_time_dict)
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
    loss_work_time_dict = {}

    try:
        year_month = input("请输入要查询的年月份(例如2023.8或8，仅查询当年月份，可空，默认为当月)")
        browser = get_current_default_browser()
        browser, origin_url = auto_login(browser)
        set_cookie(browser)
        work_time_dict = get_work_time(origin_url)
        work_time_info, work_time_header, work_time_value = total_time_to_file(work_time_dict)
        show_work_report(work_time_info, year_month)
        # print(table_csv_string)
        show_work_report_analysis(work_time_value)
        # write_to_file(table_csv_string, calculate_header, calculate_value)
        write_to_file(work_time_info, work_time_header, work_time_value)

        # work_list = ['日期\t请假类型\t请假时间\t工时\t加班时间\t在岗时长\t漏填日报\n', '2023-08-01\t\t\t11.4\t3.40\t11.41\t0.00\n', '2023-08-02\t串休假\t1.0\t8.1\t1.10\t8.1\t0.00\n', '2023-08-03\t\t\t8.0\t0.00\t8.03\t0.00\n', '2023-08-04\t\t\t9.18\t1.18\t9.18\t0.00\n', '2023-08-07\t\t\t8.0\t0.00\t8.03\t0.00\n', '2023-08-08\t\t\t8.15\t0.15\t8.15\t0.00\n', '2023-08-09\t\t\t11.0\t3.00\t11.05\t0.00\n', '2023-08-10\t\t\t8.3\t0.30\t8.33\t0.00\n', '2023-08-11\t事假\t1.0\t7.5\t0.50\t4.55\t0.00\n', '2023-08-14\t\t\t12.0\t4.00\t12.06\t0.00\n', '2023-08-15\t串休假\t1.0\t8.2\t1.20\t8.25\t0.00\n', '2023-08-16\t\t\t8.3\t0.30\t8.36\t0.00\n', '2023-08-17\t事假\t1.0\t7.6\t0.60\t7.66\t0.00\n', '2023-08-18\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-19\t\t\t2.0\t2.0\t\t\n', '2023-08-21\t\t\t9.1\t1.10\t9.13\t0.00\n', '2023-08-22\t事假\t1.0\t9.16\t2.16\t9.16\t0.00\n', '2023-08-23\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-24\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-25\t事假\t5.0\t3.0\t0.00\t3.0\t0.00\n', '2023-08-28\t\t\t8.1\t0.10\t8.11\t0.00\n', '2023-08-29\t\t\t8.1\t0.10\t8.16\t0.00\n', '2023-08-30\t年假\t1.0\t0.0\t0.00\t7.33\t7.00\n']
        # show_work_report(work_list)

        loss_time = calculate_loss_time(loss_work_time_dict)
        print(loss_time)
        if len(loss_time) != 0:
            keys, key_for_choose, _chooses = loss_time[0], loss_time[1], loss_time[2]
            # print("_keys", keys)
            # print("_key_for_choose", key_for_choose)
            # print("_chooses", _chooses)
            log_work_time(browser, keys, key_for_choose, _chooses)

            re_cat = input("是否重新查看工作报告：Y/N")
            if re_cat == "Y" or re_cat == "y":
                work_time_dict = get_work_time(origin_url)
                work_time_info, work_time_header, work_time_value = total_time_to_file(work_time_dict)
                show_work_report(work_time_info, year_month)
                # print(table_csv_string)
                show_work_report_analysis(work_time_value)
                # write_to_file(table_csv_string, calculate_header, calculate_value)
                write_to_file(work_time_info, work_time_header, work_time_value)

        browser.quit()
    except Exception as e:
        log_file = open("error.log", "a+")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3], e, file=log_file)
        log_file.close()

    while True:
        input_string = input("输入Enter退出")
        if input_string + "1" != "":
            sys.exit()

# test_url()