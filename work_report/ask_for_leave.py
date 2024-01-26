# {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Cookie": "00000000-0000-0000-0000-000000000000.widgetState=false; iTalent-tenantId=608839; user_polling_timespace_608839=0; isItalentLogin=; key-610491161=false; loginBackgroundIndex=2; Tita_PC=jsElRUfJnd_JsVtwAKhMcyAC8zzqKNhpOtRtCxdqzQwuWTS4kzMk1RI-Yt4wja8N; ssn_Tita_PC=jsElRUfJnd_JsVtwAKhMcyAC8zzqKNhpOtRtCxdqzQwuWTS4kzMk1RI-Yt4wja8N",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# }


# string = '1.0 + 1.0 = 2.0'
# if "=" in string:
#     print(string.split("= ")[1])
#
#
# a, b = []
#
# import msvcrt
#
# def hide_input_password():
#     password = ''
#     print('请输入密码：', end='', flush=True)
#     while True:
#         ch = msvcrt.getch().decode()
#         if ch == '\r':
#             break
#         elif ch == '\b':
#             if len(password) > 0:
#                 password = password[:-1]
#                 print('\b \b', end='', flush=True)
#         else:
#             password += ch
#         print('*', end='', flush=True)
#     return password
#
# password = hide_input_password()

# import stdiomask
#
# password = stdiomask.getpass(prompt='PW: ', mask='*')
# print(password)

"""
loss_work_time = {'2024-01-04': ['8.1'], '2024-01-05': ['8.81'], '2024-01-08': ['1.88']}

"""
import re

import requests

loss_work_time = {'2024-01-04': ['8.1'], '2024-01-05': ['8.81'], '2024-01-08': ['1.88']}

# def calculate_loss_time():
#     if loss_work_time == {}:
#         return []
#
#     chooses = list(loss_work_time.keys())
#
#     chooses = chooses[:len(chooses) - 1]
#     print(chooses)
#
#     while len(chooses) != 0:
#         print(" ".join([f"{index}.{chooses[index]} " for index in range(len(chooses))]))
#         what_input = input("请选择填写日报日期序号(按非数字键退出)：")
#         if not what_input.isdigit():
#             print("非数字")
#             return 0
#         choose_index = eval(what_input)
#         if choose_index not in range(len(chooses)):
#             print("请输入有效的序号")
#             continue
#
#         print(f"您选择的序号是：{choose_index}")
#         print("value is ", loss_work_time[chooses[choose_index]][-1])
#         break
#     return chooses

# calculate_loss_time()

# input_work_hours = input("请输入要登记的时间(可空，填入全部在岗时间)：")
# input_work_comments = input("请输入要登记的注释（可空）：")
# loss_work_time_1 = "8.1"
# if input_work_hours == "":
#     input_work_hours = loss_work_time_1
#
# if eval(input_work_hours) < float(loss_work_time_1):
#     print("OK")


# residue_time = float("%.2f" % 0 if (float(0.38) - float(0) - float(8.08)) <= 0 else float(0.38) - float(0) - float(8.08))
# if residue_time == 0:
#     print("OK")

# import os
# import shutil
# from prettytable import PrettyTable
#
# # 创建一个prettytable对象
# table = PrettyTable(["姓名", "年龄", "城市"])
# table.add_row(["张三", 28, "北京"])
# table.add_row(["李四", 25, "上海"])
# table.add_row(["王五", 22, "深圳"])
#
# # 获取prettytable的宽度和高度
# rows, columns = shutil.get_terminal_size()
#
# # 计算prettytable的最大宽度和高度
# max_width = max([len(str(cell)) for row in table for cell in row])
# max_height = len(table.rows) + 1
#
# # 根据最大宽度和高度调整命令行窗口的大小
# if max_width > columns:
#     os.system(f"mode con cols={max_width}")
# if max_height > rows:
#     os.system(f"mode con lines={max_height}")
#
# # 输出prettytable
# print(table)


"""
loss_work_time = {'2024-01-04': ['8.1'], '2024-01-05': ['8.81'], '2024-01-08': ['1.88']}

"""
# loss_work_time = {'2024-01-04': ['0'], '2024-01-05': ['8.81'], '2024-01-08': ['1.88']}
#
# def calculate_loss_time(loss_work_time):
#     if loss_work_time == {}:
#         return []
#
#     chooses = list(loss_work_time.keys())
#
#     # if value = 0,return
#     for index, choose in enumerate(chooses):
#         print(index)
#         print(choose)
#         print(loss_work_time[choose])
#         if loss_work_time[choose][-1] == '0':
#             chooses.pop(index)
#
#     return chooses
#
# print(calculate_loss_time(loss_work_time))

# import re
#
# filter_pattern = r"build"
# string = r'D:\fb_workspace\services\core\music\FunnAdapter\build\test-results\testDebugUnitTest\binary'
# match = re.findall(filter_pattern, string)
# print(match)
# string = '<testsuite name="com.mxsdk.personality.service.ExampleUnitTest" tests="8" skipped="0" failures="0" errors="0" timestamp="2024-01-16T14:14:36" hostname="DESKTOP-KPOKPOP" time="0.005">'
# tests_total = string.split(" ")[2].split('tests=')[1]
# print(tests_total)
# def is_same_and_zero(bin_num1, bin_num2):
#     result = bin_num1 & bin_num2
#     return result == 0
#
# bin_num1 = int('110', 2)
# bin_num2 = int('111', 2)
# print(is_same_and_zero(bin_num1, bin_num2))

datas = {'日期': ['2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-08', '2024-01-09', '2024-01-10',
                  '2024-01-11', '2024-01-12', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'],
         '请假类型': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
         '请假时间': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
         '工时': [9.1, 8.13, 8.1, 8.81, 8.08, 8.31, 8.28, 8.03, 8.38, 8.05, 14.33, 8.4, 0],
         '加班时间': [1.1, 0.13, 0.1, 0.81, 0.08, 0.31, 0.28, 0.03, 0.38, 0.05, 6.33, 0.4, 0],
         '在岗时长': [9.18, 8.13, 8.1, 8.81, 8.08, 8.31, 8.28, 8.03, 8.38, 8.05, 14.33, 8.4, 5.93],
         '漏填日报': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.93],
         '上班打卡': ['09:09:59', '09:29:04', '08:48:19', '08:50:23', '08:44:36', '08:38:01', '08:50:49', '08:52:57',
                      '08:53:34', '08:57:51', '08:47:56', '11:20:52', '08:45:57'],
         '下班打卡': ['19:30:04', '18:39:18', '17:57:18', '18:40:10', '18:23:40', '17:57:24', '18:13:21', '17:55:34',
                      '18:49:17', '18:02:25', '00:09:06', '21:07:17', '12:39:56'],
         '迟到未请假': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.5, 0],
         '加班串休': ['迟到不足30分钟，迟到次数还剩1', '迟到不足30分钟，迟到次数还剩0', '', '', '', '', '', '', '', '',
                      '打车可报销\n明天可串休3h', '打车可报销', '']}
import json
def sendto_feishu(datas):
    print(datas)
    json_data = json.dumps(datas, ensure_ascii=False)
    # ctp_AAiDuD3JOgTI
    headers = {'Content-Type': 'application/json'}
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/32cb487b-194f-4a52-8c15-f6a093f71a64"
    message_json = {
        "msg_type": "text",
        "content": {
            "text": json_data
        }
    }
    response = requests.post(url, json=message_json, headers=headers)
    print(response)
    print(response.status_code)

# sendto_feishu(datas)

message = {
    "msg_type": "interactive",
    "card": {
        "elements": [{
                "tag": "div",
                "text": {
                        "content": "日报查询[看]",
                        "tag": "lark_md"
                }
        }, {
                "actions": [{
                        "tag": "button",
                        "text": {
                                "content": "redmine",
                                "tag": "lark_md"
                        },
                        "url": "http://redmine-pa.mxnavi.com/workreports",
                        "type": "default",
                        "value": {}
                },
                    {
                        "tag": "button",
                        "text": {
                            "content": "请假",
                            "tag": "lark_md"
                        },
                        "url": "https://www.italent.cn/portal/iTalentHome/",
                        "type": "default",
                        "value": {}
                    }
                ],
                "tag": "action"
        }],
        "header": {
                "title": {
                        "content": "每日日报查询",
                        "tag": "plain_text"
                }
        }
    }
}

headers = {'Content-Type': 'application/json'}
url = "https://open.feishu.cn/open-apis/bot/v2/hook/32cb487b-194f-4a52-8c15-f6a093f71a64"
# url = "https://open.feishu.cn/open-apis/bot/v2/hook/61eab52f-c826-4d33-a151-e5f4b4b46e9e"
response = requests.post(url, json=message, headers=headers)