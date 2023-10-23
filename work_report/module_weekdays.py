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


def get_first_and_end_day_by_month(input_month):
    today_date = get_today_date()
    target_year = today_date.year
    target_month = today_date.month
    if input_month != "":
        if "." in input_month:
            year_month = input_month.split(".")
            target_year = int(year_month[0])
            target_month = int(year_month[1])
        else:
            target_month = int(input_month)

        if target_month > 12:
            target_month = today_date.month
        last_day = calendar.monthrange(target_year, target_month)[1]
    else:
        last_day = today_date.day

    # print(target_year)
    # print(target_month)
    # last_day = calendar.monthrange(target_year, target_month)
    start_date = datetime.datetime(target_year, target_month, 1)
    last_date = datetime.datetime(target_year, target_month, last_day)
    return [start_date.date(), last_date.date()]


def get_start_end_days_string_by_month(input_month):
    target_date = get_first_and_end_day_by_month(input_month)

    day_format = '%Y-%m-%d'
    return [target_date[0].strftime(day_format), target_date[1].strftime(day_format)]


def get_today_date():
    today = get_today()
    return datetime.datetime.strptime(today, '%Y-%m-%d')


def get_today():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


def get_workdays():
    start_end_days = get_first_and_end_day_of_month()
    return chinese_calendar.get_workdays(start_end_days[0], start_end_days[1])


def get_workdays_by_month(input_month):
    start_end_days = get_first_and_end_day_by_month(input_month)
    return chinese_calendar.get_workdays(start_end_days[0], start_end_days[1])


def is_workday(date):
    try:
        if isinstance(date, str):
            date_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        else:
            date_date = date
        return chinese_calendar.is_workday(date_date)
    except Exception as e:
        print("格式错误: ", e)
        return True


def get_format_dates(start_day, end_day):
    dates = [start_day + datetime.timedelta(days=x) for x in range((end_day - start_day).days + 1)]
    formatted_dates = [date.strftime('%Y-%m-%d') for date in dates]

    # print(formatted_dates)
    return formatted_dates


def get_days_until_today():
    today = datetime.date.today()
    first_day = datetime.date(today.year, today.month, 1)
    return get_format_dates(first_day, today)


def get_days_until_today_with_month(input_month):
    today = get_today_date()
    # print(today)
    # print(today.month)
    if input_month != "" and int(input_month) != today.month:
        start_day, end_day = get_first_and_end_day_by_month(input_month)
    else:
        start_day = datetime.date(today.year, today.month, 1)
        end_day = datetime.date(today.year, today.month, today.day)

    # print(start_day)
    # print(end_day)
    return get_format_dates(start_day, end_day)


if __name__ == "__main__":
    # year_month = input("请输入要查询的年月份(例如2023.8或8，仅查询当年月份，可空，默认为当月)")
    # print(get_start_end_days_string_by_month(year_month))
    # print(get_days_until_today_with_month(""))
    # print("-------------")
    # print(get_days_until_today())

    # work_days = get_days_until_today_with_month("9")
    # print(work_days)
    work_date = datetime.date(2023, 10, 7)
    print(work_date)
    print(get_workdays())
    print(work_date in get_workdays())
