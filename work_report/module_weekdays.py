import chinese_calendar


import calendar
import datetime
import time

def get_first_and_end_day_of_month():
    today_date = get_today_date()
    last_day = calendar.monthrange(today_date.year, today_date.month)
    start_date = datetime.datetime(today_date.year, today_date.month, last_day[0])
    last_date = datetime.datetime(today_date.year, today_date.month, last_day[1])
    return [start_date.date(), last_date.date()]

def get_start_end_days_string():
    days = get_first_and_end_day_of_month()
    day_format = '%Y-%m-%d'
    return [days[0].strftime(day_format), days[1].strftime(day_format)]

def get_today_date():
    today = get_today()
    return datetime.datetime.strptime(today, '%Y-%m-%d')


def get_today():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


def get_workdays():
    start_end_days = get_first_and_end_day_of_month()
    return chinese_calendar.get_workdays(start_end_days[0], start_end_days[1])


def is_workday(date):
    try:
        if type(date) == "str":
            date_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        else:
            date_date = date
        return chinese_calendar.is_workday(date_date)
    except Exception as e:
        print("格式错误: ", e)
        return ""
