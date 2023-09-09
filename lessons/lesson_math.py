"""
数学计算模块
ceil(x) 返回大于或等于x的最小整数
floor(x) 返回小于或等于x的最大整数
sqrt(x) x的平方根
pow(x, y) x的y次方
log(x[, base]) 返回以base为底的x对数，若base为空，则为x的自然对数
sin(x) 弧度x的三角正弦
degree(x) 将弧度转化为角度
radians(x) 将角度转化成弧度


日期时间模块--datetime

datetime  包含时间和日期
date      包含日期
time      只包含时间
timedelta 时间跨度
tzinfo    时区

datetime。datetime(year, month, day[, hour, minute, second, microsecond, tzinfo])

常用方法：
datetime.today():返回当前的本地日期和时间
datetime.now(tz=None) 返回指定时区的当前日期和时间，参数用于设置时区，如果参数省略则方法等同于today
datetime.fromtimestamp(timestamp, tz=None) 返回与unix时间戳对应的本地日期和时间

date类

datetime。date(year, month, day)
date.today()
date.fromtimestamp(timestamp)


time类

datetime。time(hour, minute, second, microsecond, tzinfo)

计算时间跨度类---timedelta

datetime.timedelta(days, seconds, microseconds,milliseconds, minutes, hours, weeks)


日期与字符串相互转换

datetime、date、time都有一个实力方法.strftime(format)

字符串转换成日期：
datetime。strptime(date_string, format)

日期格式控制符

%m 两位月
%y 两位年
%Y 四位年
%d 两位天
%H 两位小时，24小时制
%M 两位分钟
%S 两位秒
%I 两位小时，12小时制
%p AM和PM区域性设置，AM和PM
%f 以6位数表示微秒
%z +HHMM或-HHMM形式的UTC偏移 +0000、-0400，如果没有设置时区就为空
%Z 时区名称 UTC、EST、CST，如果没有设置时区，则为空

正则表达式  re
"""
import math
import datetime

print(math.degrees(math.pi))
today = datetime.datetime.today()
today_string = today.strftime("%Y-%m-%d %I:%M:%S.%f")
print(today_string)
print()

# 转换需要和字符串格式一致
today_date = datetime.datetime.strptime(today_string, "%Y-%m-%d %I:%M:%S.%f")
print(today_date)
