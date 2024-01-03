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
    target_year, target_month, last_day = input_month

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


def get_current_month():
    return time.localtime(time.time()).tm_mon


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
    # print(today)
    # print(today.month)
    start_day, end_day = get_first_and_end_day_by_month(input_month)
    # print(start_day)
    # print(end_day)
    return get_format_dates(start_day, end_day)


def in_three_month(input_month):
    today = datetime.datetime.now()
    today_year = today.year
    today_month = today.month
    # print(f"current_year is {current_year}")
    target_year = today_year

    if input_month == "":
        return [today_year, today_month, today.day]

    two_month_ago = today_month - 2
    if two_month_ago <= 0:
        two_month_ago += 12
        target_year -= 1
    months = [two_month_ago, two_month_ago + 1 if two_month_ago + 1 <= 12 else 1, today_month]
    # print(f"months is {months}")

    year_month = input_month.split(".")
    # print(f"year_month is {year_month}")

    if len(year_month) == 1:
        input_month = int(year_month[0])
        if input_month > 12:
            input_month = today_month
        elif input_month not in months or input_month > today_month:
            return None

        last_day = calendar.monthrange(today_year, input_month)[1]
        return [today_year, input_month, last_day]

    input_year = int(year_month[0])
    input_month = int(year_month[1])
    if input_month > 12:
        input_month = today_month
    elif input_year not in [today_year, target_year] or input_month not in months:
        return None

    if not datetime.datetime(target_year, two_month_ago, 1) <= datetime.datetime(input_year, input_month, 1) <= today:
        return None
    last_day = calendar.monthrange(input_year, input_month)[1]
    return [input_year, input_month, last_day]


if __name__ == "__main__":
    # year_month = input("请输入要查询的年月份(例如2023.8或8，仅查询当年月份，可空，默认为当月)")
    # print(get_start_end_days_string_by_month(year_month))
    # print(get_days_until_today_with_month(""))
    # print("-------------")
    # print(get_days_until_today())

    # work_days = get_days_until_today_with_month("9")
    # print(work_days)
    # work_date = datetime.date(2023, 10, 7)
    # print(work_date)
    # print(get_workdays())
    # print(work_date in get_workdays())
    # print(time.localtime(time.time()).tm_mon)
    # today_date = get_today_date()
    # target_year = today_date.year
    # target_month = today_date.month
    # start_date = datetime.datetime(target_year, target_month, 1)
    #
    # start_date_yesterday = start_date - datetime.timedelta(days=1)
    # start_date_yesterday_month = start_date_yesterday.month
    # start_date_yesterday_year = start_date_yesterday.year

    import calendar
    # 获取当前月份和年份
    tests = ["2024.1", "2023.12","2023.11","2023.1","2024.10","2022.12", "8", "10", "12", "1", "2", "3", "2024.12"]
    for demo in tests:
        result = in_three_month(demo)
        print(f"current_month is {demo}")
        print(f"result is {result}")
    result_time = in_three_month("")
    get_workdays_by_month(result_time)
    # result = in_three_month(tests[2])
    # get_days_until_today_with_month(result)