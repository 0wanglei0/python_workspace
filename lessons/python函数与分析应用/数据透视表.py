# -*- coding: utf-8 -*-

import pandas as pd

pivot_data = pd.read_excel('datas.xlsx')
print(pivot_data.head())
print(pivot_data.describe(include='all').T)

# 透视表 pivot_table
import numpy as np

# 求内容5总和
result = pivot_data.pivot_table(index=['内容2'], values=['内容5'], aggfunc=np.sum)
print(result.head())

# 求内容5的均值
result = pivot_data.pivot_table(index=['内容2'], values=['内容5'], aggfunc=np.mean)
print(result.head())

# index是内容，value是计算的
result = pivot_data.pivot_table(index='内容2', values='内容4', aggfunc=np.count_nonzero)
print(result.head())

result = pivot_data.pivot_table(index=['内容2'], values=['内容5', '内容4'], aggfunc={'内容5': np.sum, '内容4': np.count_nonzero})
print(result.head())
