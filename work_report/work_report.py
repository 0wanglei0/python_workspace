# -*- coding: utf-8 -*-
import os
import platform
import re
import sys
import datetime
import time
import traceback

import pandas
from bs4 import BeautifulSoup
from lxml import etree
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

from log_print import Log
import argparse

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': "gzip, deflate",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

""" ..\python_workspace\Scripts\pyinstaller.exe -F .\work_report.py --add-binary "chromedriver.exe;." --add-binary "chromedriver_116.exe;." --add-binary "chromedriver_115.exe;." """


def auto_login(local_browser):
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

    log.info_out("页面加载中，请稍后...")
    time.sleep(2)
    return [local_browser, url]


def set_cookie(local_browser):
    cookie = local_browser.get_cookies()[0].get("value")
    headers["Cookie"] = "_redmine_session=" + cookie


def find_work_time(response_with_code):
    resp_html = etree.HTML(response_with_code.content)
    # print(resp_html)
    resp_list = resp_html.xpath("//table[@id='workreport-table']/tbody")
    # print(resp_list)
    # print("in")
    result = str(resp_list[0].xpath("//tr")[-1].xpath("./td/text()")[-1]).replace("\n", "").replace(" ", "")
    # print(result)
    return result


def get_time_at_company(input_month):
    log.info_out("统计在岗时间")
    response = requests.get("https://redmine-pa.mxnavi.com/cardinfos", headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    hidden_code = soup.find(name="input", attrs={"name": "code"})["value"]
    # print("hidden_code", hidden_code)
    # print(soup)
    work_days = weekdays.get_days_until_today_with_month(input_month)
    work_time_by_days = {}
    for workday in work_days:
        url = f"https://redmine-pa.mxnavi.com/selectcardinfo?utf8=%E2%9C%93&code={hidden_code}" \
              f"&event_time%5B%5D={workday}&commit=%E6%9F%A5%E8%AF%A2"
        # print(url)
        response_with_code = requests.get(url, headers=headers)

        worktime = find_work_time(response_with_code)
        work_time_by_days[workday] = worktime
        time.sleep(0.2)
    log.info(work_time_by_days)
    return work_time_by_days


def get_work_time(url):
    # print(browser.get_cookies())
    log.info_out("统计已登记日报")
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


def total_time_to_file(table_dic, input_month):
    log.info_out("统计时间制成表格")
    # print(table_dic)
    print_lst = [
        str("日期" + "\t" + "请假类型" + "\t" + "请假时间" + "\t" + "工时" + "\t" + "加班时间" + "\t" + "在岗时长" + "\t" + "漏填日报" + "\n")]
    fill_value = table_dic.get("values")
    workday = 0
    external_work = float(0)
    holiday_time = 0
    work_at_weekend = []
    for item in fill_value:
        log.d("work_item: ", item)

        if len(item) != 13:
            if len(item) == 10 and item[4] == '' and item[7] == '':
                if item[1] == "事假" or item[1] == "病假":
                    holiday_time += float(item[5])
                last_item = print_lst[len(print_lst) - 1].split("\t")
                current_day_total = float(item[5]) + float(last_item[3])
                current_holiday_type = item[1] if last_item[1] == "" else last_item[1]
                current_holiday_time = item[5]
                last_external_work_time = float(last_item[4])

                log.d("current_holiday_time 1", current_holiday_time)
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
                log.d("latest_item", new_item_string)
                # print("item", item)
            continue
        if item[5] == '':
            workday += 1
            if item[2] == "事假" or item[2] == "病假":
                holiday_time += float(item[6])
            current_external_work_time = 0 if (float(item[7]) + float(item[6]) - 8) < 0 else float(item[7]) + float(
                item[6]) - 8
            external_work += current_external_work_time
            log.d("current_external_work_time", current_external_work_time)
            log.d("external_work", external_work)
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
            work_date = datetime.date(year, month, day)
            log.info(work_date)
            if not weekdays.is_workday(work_date):
                external_work += float(item[7])
                print_lst.append(str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[7] + "\t" + item[7]
                                     + "\t" + item[7] + "\t" + str("%.2f" % (float(item[8]) - float(item[7]))) + "\n"))
                work_at_weekend.append(item[0])
                log.info("date in holiday")
            else:
                workday += 1
                external_work += float("%.2f" % (0 if float(item[7]) - 8 < 0 else float(item[7]) - 8))
                print_lst.append(
                    str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[7]
                        + "\t" + str("%.2f" % (0 if float(item[7]) - 8 < 0 else float(item[7]) - 8)))
                    + "\t" + item[8]
                    + "\t" + str("%.2f" % (0 if 8 - float(item[7]) < 0 else 8 - float(item[7]))) + "\n")
                log.info("date in workday")

    log.d("workday", workday)

    log.d("external_work ", str("%.2f" % external_work))
    log.d("holiday_time", holiday_time)
    log.d("external_work: ", external_work)
    holiday_hour = external_work // 20 * 8
    log.d("holiday_hour: ", holiday_hour)
    log.info(print_lst)
    expect_worktime = len(weekdays.get_workdays_by_month(input_month)) * 8
    calculate_header = ["当前负荷", "预计加班时间", "已加班", "请假合计", "可串休", "剩余串休", "扣工资工时"]
    calculate_value = [str("%.3f" % float(external_work / expect_worktime + 1)), "",
                       str("%.2f" % external_work), holiday_time, holiday_hour,
                       str("%.2f" % (0 if holiday_hour - holiday_time < 0 else holiday_hour - holiday_time)),
                       "0" if holiday_time - holiday_hour < 0 else str("%.2f" % (holiday_time - holiday_hour))]

    return [print_lst, calculate_header, calculate_value, work_at_weekend]


def write_to_excel(detail_datas, analysis_datas):
    log.info_out("写入文件")
    rows_num = len(detail_datas["日期"]) + 3
    df0 = pandas.DataFrame(detail_datas)
    df1 = pandas.DataFrame(analysis_datas)
    # print(df0)

    df0.convert_dtypes()
    df1.convert_dtypes()
    with pandas.ExcelWriter("work_report.xlsx", engine='xlsxwriter') as writer:
        df0.to_excel(writer, sheet_name="work_report", index=False, startrow=0)
        df1.to_excel(writer, sheet_name="work_report", index=False, startrow=rows_num)


def write_to_file(calculate_header, calculate_value):
    with open("work_report.xlsx", "w+", encoding="utf8") as wr:
        # wr.write(print_lst.replace(",", "\t"))
        # for string in print_lst:
        #     wr.write(string)

        wr.write("\n")
        wr.write("\n")
        wr.write("\n")
        for header in calculate_header:
            wr.write(header + "\t")
        wr.write("\n")

        for c_value in calculate_value:
            wr.write(str(c_value) + "\t")
        wr.write("\n")


def calculate_loss_time(loss_work_time):
    if loss_work_time == {}:
        log.info("没有需要填写的日报")
        return []

    _key_for_choose = []
    _keys = list(loss_work_time.keys())
    chooses = []
    log.info(_keys)
    input_date = weekdays.get_first_and_end_day_by_month(year_month)
    key_len = len(_keys) - 1
    if input_date[0].month != weekdays.get_current_month():
        key_len = len(_keys)
    for index in range(key_len):
        choose = f"{index}.{_keys[index]}"
        chooses.append(choose)
        _key_for_choose.append(_keys[index])
    return [_keys, _key_for_choose, chooses]


def log_work_time(local_browser, _keys, _key_for_choose, _chooses):
    log.d("_keys", _keys)
    log.d("_key_for_choose", _key_for_choose)
    log.d("_chooses", _chooses)
    while len(_chooses) != 0:
        log.info_out(_chooses)
        what_input = input("请选择填写日报日期序号(按非数字键退出)：")
        pattern = r"\d+"
        matches = re.findall(pattern, what_input)
        if what_input == "q" or len(matches) == 0:
            return 0
        choose_index = eval(matches[0])
        if choose_index < 0 or choose_index > len(_key_for_choose):
            log.info_out("请输入有效的序号")
            continue

        log.info_out(f"您选择的序号是：{_chooses[choose_index]}")
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
        log.info_out(day_logged_time)

        input_work_hours = input("请输入要登记的时间(可空，填入全部在岗时间)：")
        input_work_comments = input("请输入要登记的注释（可空）：")
        if input_work_hours == "":
            residue_time = float(total_time) - float(logged_time)
            if residue_time < 0:
                log.info_out("日报已填写")
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
            log.info_out("日报填写完成")
            return 1
        else:
            is_goon = input("是否继续填写日报 Y/N")
            if is_goon == "Y" or is_goon == "y":
                continue
            else:
                log.info_out("日报填写完成，结束运行")
                return 1
    else:
        return 0


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
    log.info_out("浏览器加载中，请稍后...")
    # print(get_current_system() == "Windows")
    # print(judge.init_edge())
    this_browser = None
    if get_current_system() == "Windows" and judge.init_edge():
        this_browser = webdriver.Edge()
        log.info_out("使用Edge")

    if this_browser is None:
        this_browser = webdriver.Chrome(service=Service(executable_path=cdu.get_report_by_chrome()))
        log.info_out("使用Chrome")

    if this_browser is None:
        log.info_out("没有找到合适的浏览器")
        return None

    return this_browser


def get_current_system():
    return platform.system()


def show_work_report(work_list, worktime_by_days_dict, work_at_weekend):
    # print(work_list)
    tb = ptb.PrettyTable()
    tb.field_names = work_list[0].replace("\n", "").split("\t")
    new_list = work_list[1::]
    rows = []
    external_work = 0
    for item in new_list:
        field_item = item.replace("\n", "").split("\t")
        log.info(field_item)
        lst = [field_item[0], field_item[1], field_item[2], field_item[3], field_item[4], field_item[5], field_item[6]]
        log.info(lst)
        actual_time = field_item[5] if field_item[5] > field_item[3] else field_item[3]
        if field_item[2] != "":
            if "=" in field_item[2]:
                _external = eval(field_item[2].split("= ")[1]) + eval(actual_time) - 8
            else:
                _external = eval(field_item[2]) + eval(actual_time) - 8
        else:
            if field_item[0] in work_at_weekend:
                _external = eval(actual_time)
            else:
                _external = eval(actual_time) - 8

        external_work += 0 if _external < 0 else _external

        rows.append(lst)
        date_date = field_item[0].split("-")
        date = datetime.date(int(date_date[0]), int(date_date[1]), int(date_date[2]))
        if field_item[6] != "" and field_item[6] != "0.00":
            remain_work_time = float(field_item[5]) - float(field_item[3])
            if remain_work_time < float(field_item[6]):
                log.info_out(f"{field_item[0]} 是请假了吗？记得请假哦")
            elif float(remain_work_time) > 0.2:
                loss_work_time_dict[field_item[0]] = [field_item[2], field_item[3], field_item[5]]

        if len(worktime_by_days_dict) != 0:
            worktime_by_days_dict.pop(date.strftime("%Y-%m-%d"))

    if len(worktime_by_days_dict) != 0:
        for key in worktime_by_days_dict.keys():
            # 当周末加班但是没填工时时，应该作为候选
            # if key in work_at_weekend:
            #     continue
            value = worktime_by_days_dict[key]
            if value == '0.0':
                continue
            loss_list = [key, "", "", "", "", value, value]
            loss_work_time_dict[key] = [value]

            if weekdays.is_workday(key):
                _external = eval(value) - 8
            else:
                _external = eval(value)

            external_work += 0 if _external < 0 else _external
            rows.append(loss_list)

    rows.sort(key=lambda i: i[0], reverse=False)
    tb.add_rows(rows)
    log.info_out("请查看：")
    log.info_out(tb)
    datas = {
        tb.field_names[0]: list(item[0] for item in rows),
        tb.field_names[1]: list(item[1] for item in rows),
        tb.field_names[2]: list(item[2] for item in rows),
        tb.field_names[3]: list(eval(item[3]) if item[3] != "" else 0 for item in rows),
        tb.field_names[4]: list(eval(item[4]) if item[4] != "" else 0 for item in rows),
        tb.field_names[5]: list(eval(item[5]) if item[5] != "" else 0 for item in rows),
        tb.field_names[6]: list(eval(item[6]) if item[6] != "" else 0 for item in rows)
    }

    return external_work, datas


def show_work_report_analysis(work_total):
    tb_total = ptb.PrettyTable()
    tb_total.field_names = ["当前负荷", "预计加班时间", "已加班", "请假合计", "可串休", "剩余串休", "扣工资工时"]
    tb_total.add_row(work_total)
    log.info_out(tb_total)
    datas = {
        tb_total.field_names[0]: [work_total[0]],
        tb_total.field_names[1]: [work_total[1]],
        tb_total.field_names[2]: [work_total[2]],
        tb_total.field_names[3]: [work_total[3]],
        tb_total.field_names[4]: [work_total[4]],
        tb_total.field_names[5]: [work_total[5]],
        tb_total.field_names[6]: [work_total[6]]
    }
    return datas


def get_external_worktime(worktime_by_days_dict):
    total = 0
    for key in worktime_by_days_dict.keys():
        total += 0 if eval(worktime_by_days_dict[key]) - 8 < 0 else eval(worktime_by_days_dict[key]) - 8
    return total


def parse_args():
    parser = argparse.ArgumentParser(description='这是一个示例程序')

    # 添加参数
    parser.add_argument('--log', type=int, help='一个整数', default=0)
    # 解析参数
    args = parser.parse_args()
    # 使用参数
    return args.log


# ios 运行可能要在mac上运行pyinstaler
# windows
#  ..\python_workspace\Scripts\pyinstaller.exe -F .\work_report.py
#  --add-binary "chromedriver.exe;." --add-binary "chromedriver_116.exe;."
#  --add-binary "chromedriver_115.exe;."
if __name__ == '__main__':
    loss_work_time_dict = {}
    log = Log(parse_args())

    try:
        year_month = input("请输入要查询的年月份(例如2023.8或8，仅查询当年月份，可空，默认为当月)")
        browser = get_current_default_browser()
        if browser is None:
            log.info_out("结束运行")
            sys.exit()

        log.info_out("加载完成！")
        browser, origin_url = auto_login(browser)
        set_cookie(browser)
        log.info_out("登录成功")
        # 好像只能这样了，请假的
        work_time_by_days_dict = get_time_at_company(year_month)
        log.info_out("在岗时间统计完成")
        # work_time_by_days_dict = {'2023-09-01': '8.33', '2023-09-02': '0.0', '2023-09-03': '0.0', '2023-09-04': '10.15', '2023-09-05': '11.73', '2023-09-06': '7.61', '2023-09-07': '5.48', '2023-09-08': '8.08', '2023-09-09': '0.0', '2023-09-10': '0.0', '2023-09-11': '2.41'}
        work_time_dict = get_work_time(origin_url)
        log.info_out("统计已登记日报完成")
        # print(work_time_dict)
        work_time_info, work_time_header, work_time_value, work_weekend = total_time_to_file(work_time_dict, year_month)
        log.info_out("表格制作完成")
        _external_work, _datas = show_work_report(work_time_info, work_time_by_days_dict, work_weekend)
        # print(table_csv_string)
        # print(_external_work)
        # print(work_time_value)
        work_time_value[1] = "%.2f" % _external_work
        _datas_analysis = show_work_report_analysis(work_time_value)
        # print("%.2f" % _external_work)
        # print(work_time_value)
        # write_to_file(table_csv_string, calculate_header, calculate_value)
        # write_to_excel(_datas, _datas_analysis)
        # write_to_file(work_time_info, work_time_header, work_time_value)

        # work_list = ['日期\t请假类型\t请假时间\t工时\t加班时间\t在岗时长\t漏填日报\n', '2023-08-01\t\t\t11.4\t3.40\t11.41\t0.00\n', '2023-08-02\t串休假\t1.0\t8.1\t1.10\t8.1\t0.00\n', '2023-08-03\t\t\t8.0\t0.00\t8.03\t0.00\n', '2023-08-04\t\t\t9.18\t1.18\t9.18\t0.00\n', '2023-08-07\t\t\t8.0\t0.00\t8.03\t0.00\n', '2023-08-08\t\t\t8.15\t0.15\t8.15\t0.00\n', '2023-08-09\t\t\t11.0\t3.00\t11.05\t0.00\n', '2023-08-10\t\t\t8.3\t0.30\t8.33\t0.00\n', '2023-08-11\t事假\t1.0\t7.5\t0.50\t4.55\t0.00\n', '2023-08-14\t\t\t12.0\t4.00\t12.06\t0.00\n', '2023-08-15\t串休假\t1.0\t8.2\t1.20\t8.25\t0.00\n', '2023-08-16\t\t\t8.3\t0.30\t8.36\t0.00\n', '2023-08-17\t事假\t1.0\t7.6\t0.60\t7.66\t0.00\n', '2023-08-18\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-19\t\t\t2.0\t2.0\t\t\n', '2023-08-21\t\t\t9.1\t1.10\t9.13\t0.00\n', '2023-08-22\t事假\t1.0\t9.16\t2.16\t9.16\t0.00\n', '2023-08-23\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-24\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-25\t事假\t5.0\t3.0\t0.00\t3.0\t0.00\n', '2023-08-28\t\t\t8.1\t0.10\t8.11\t0.00\n', '2023-08-29\t\t\t8.1\t0.10\t8.16\t0.00\n', '2023-08-30\t年假\t1.0\t0.0\t0.00\t7.33\t7.00\n']
        # show_work_report(work_list)

        loss_time = calculate_loss_time(loss_work_time_dict)
        # print(loss_time)
        if len(loss_time) != 0:
            keys, key_for_choose, _chooses = loss_time[0], loss_time[1], loss_time[2]
            # print("_keys", keys)
            # print("_key_for_choose", key_for_choose)
            # print("_chooses", _chooses)
            log_result = log_work_time(browser, keys, key_for_choose, _chooses)

            if log_result != 0:
                re_cat = input("是否重新查看工作报告：Y/N")
                if re_cat == "Y" or re_cat == "y":
                    work_time_by_days_dict = get_time_at_company(year_month)

                    work_time_dict = get_work_time(origin_url)

                    work_time_info, work_time_header, work_time_value, work_weekend = total_time_to_file(work_time_dict,
                                                                                                         year_month)
                    _external_work, _datas = show_work_report(work_time_info, work_time_by_days_dict, work_weekend)
                    work_time_value[1] = "%.2f" % _external_work

                    # print(table_csv_string)
                    _datas_analysis = show_work_report_analysis(work_time_value)
                    # write_to_file(table_csv_string, calculate_header, calculate_value)
                    # write_to_file(work_time_info, work_time_header, work_time_value)
        write_to_excel(_datas, _datas_analysis)
        log.info_out("完成")
        browser.quit()
    except Exception as e:
        log.info(e)
        log_file = open("error.log", "a+")
        now = datetime.datetime.now()
        error_message = traceback.format_exc()
        log.info_out_to_file(now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3], error_message, log_file)
        log_file.close()

    while True:
        input_string = input("输入Enter退出")
        if input_string + "1" != "":
            sys.exit()

# test_url()
