# -*- coding: utf-8 -*-

# 分组 groupby
import pandas as pd

datas = pd.read_excel('test.xls', index_col='日期')
print(datas)
print(datas.groupby("日期")['工时'].sum())
print(datas.groupby("日期")['请假类型'].count())

datas = datas.drop(columns="请假类型")
datas = datas.drop(columns="请假时间")
print(datas)
# apply
# 按列应用max
print('列最大')
print(datas.apply(max, axis=0))

# 按行应用max
print('行最大')
print(datas.apply(max, axis=1))

# stack 行转换成列，unstack 列转换成行
print('旋转行')
print(datas.stack())
print('旋转列')
print(datas.unstack())