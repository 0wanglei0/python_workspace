# -*- coding: utf-8 -*-
import pandas as pd

datas = pd.read_excel("test.xls")
print(datas.head())
print(datas.describe().T)
print(datas.loc[:, '加班时间'][datas.加班时间 > 2])

print(datas.loc[9, '加班时间'])
import numpy as np

datas.loc[9, '加班时间'] = np.nan
print(datas.describe())

# 标准化
print('标准分数')
datas = datas['加班时间']
datas = datas.fillna(4.00)
print((datas - datas.mean()) / datas.std())
