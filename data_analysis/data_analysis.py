# 数据分析
"""

分析的主要内容

现状：分析已经发生了什么
原因：为什么出现这种现状
预测：预测未来可能发生什么

数据分析的基本流程

熟悉工具 1.Excel 透视图  2.Python
搭建开发环境Python、集成开发环境PyCharm，数据分析标准环境Anaconda
文学式开发工具Jupyter Notebook
科学计算工具IPython


明确目的
获取数据
数据处理
数据分析
验证结果
结果呈现
数据应用


pandas
"""
import pandas as pd
import xlrd

# pd.read_excel()

data = ["a", "b", "c"]
series = pd.Series(data, index=[1,2,3])
print(series)
series = pd.Series(data)
print(series)