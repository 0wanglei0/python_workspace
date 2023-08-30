import prettytable as ptb
import datetime
import time

tb = ptb.PrettyTable()
def show_ticket(row_num):
    tb.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]
    for i in range(row_num):
        lst = [f"第{i + 1}行", "有票", "有票", "有票", "有票", "有票"]
        tb.add_row(lst)
    print(tb)

def order_ticket(row_num, seat_num):
    row = tb[row_num - 1]
    value = row.rows[0]
    value[seat_num] = "已售"
    tb.del_row(row_num - 1)
    tb.add_row(value)
    tb.sortby = tb.field_names[0]
    print(tb)

if __name__ == "__main__":
    show_ticket(10)
    # order_ticket(5, 2)
    # date = datetime.datetime.strptime("2005-03-08", "%Y-%m-%d")
    # print(date)
    # print(str(date + datetime.timedelta(days=3)).split(" ")[0])
    # print(time.time())
    # print(time.localtime(time.time()))
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
