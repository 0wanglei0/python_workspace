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

loss_work_time = {'2024-01-04': ['8.1'], '2024-01-05': ['8.81'], '2024-01-08': ['1.88']}

def calculate_loss_time():
    if loss_work_time == {}:
        return []

    chooses = list(loss_work_time.keys())

    chooses = chooses[:len(chooses) - 1]
    print(chooses)

    while len(chooses) != 0:
        print(" ".join([f"{index}.{chooses[index]} " for index in range(len(chooses))]))
        what_input = input("请选择填写日报日期序号(按非数字键退出)：")
        if not what_input.isdigit():
            print("非数字")
            return 0
        choose_index = eval(what_input)
        if choose_index not in range(len(chooses)):
            print("请输入有效的序号")
            continue

        print(f"您选择的序号是：{choose_index}")
        print("value is ", loss_work_time[chooses[choose_index]][-1])
        break
    return chooses

calculate_loss_time()

# input_work_hours = input("请输入要登记的时间(可空，填入全部在岗时间)：")
# input_work_comments = input("请输入要登记的注释（可空）：")
# loss_work_time_1 = "8.1"
# if input_work_hours == "":
#     input_work_hours = loss_work_time_1
#
# if eval(input_work_hours) < float(loss_work_time_1):
#     print("OK")