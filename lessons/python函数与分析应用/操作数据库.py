# -*- coding: utf-8 -*-

# 数据库

# sqlite
import sqlite3

# 建表
create_table = """CREATE TABLE IF NOT EXISTS test (
    stuid varchar(10),
    stuname varchar(20),
    gender varchar(2),
    age integer
)
"""

# 使用特定的文件名（':memory:' ），在内存中创建一个数据库
conn = sqlite3.connect(':memory:')
conn.execute(create_table)
conn.commit()

cursor = conn.execute("select * from test")
print(cursor.fetchall())

# 插入数据
data = [(1, 'wang', 'male', 32), (2, 'li', 'female', 32), (3, 'wang', 'male', 3)]
insert_data = """INSERT INTO test VALUES (?, ?, ?, ?)"""
conn.executemany(insert_data, data)
conn.commit()

print("######")
cursor = conn.execute("select * from test")
print(cursor.fetchall())


import pandas.io.sql as sql

query = sql.read_sql_query('select * from test', conn)
print(query)
conn.close()

# 连接MySQL
import pymysql

con = pymysql.connect(host='localhost', user='root', password='password', db="jianli", charset="utf8")
print(con.db)

cursor = con.cursor()
sql = "select * from sys_file;"
cursor.execute(sql)
con.commit()

select_data = cursor.fetchall()
# print(select_data)

file = []
for row in select_data:
    file.append(row[1])

print(file)
con.close()