"""
需求分析
1.具备的功能
1.1 添加学生及成绩信息
1.2 学生信息保存到文件中
1.3 查询学生信息
1.4 根据学生成绩进行排序
1.5 统计学生总分

系统设计
7大模块
1.录入
2.查找
3.删除
4.修改
5.排名
6.统计总人数
7.显示全部学生模块

流程设计
用户  主界面  功能菜单  选择功能  是否继续 结束

开发必备
内置模块 os re
目录结构
students
    student.txt
    stusystem.py

主函数设计
流程：
开始  显示主菜单  选择菜单项  存在  执行对应功能  不存在 提示并显示主菜单  循环
0 退出系统
1 录入 insert
2 查找 search
3 删除 delete
4 修改 update
5 排序 sort
6 统计 total
7 显示 show

主界面运行效果图
***************学生信息管理系统***************

学生信息维护模块设计

查询、统计模块设计

排序模块设计

项目打包

"""
import os.path

import traceback
filename = "students.txt"
format_title = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
title = format_title.format("ID", "name", "english", "python", "java", "total")


def start():
    print("**************学生管理系统***************")
    print("---------------功能菜单--------------")
    print("\t\t\t\t\t 1.录入学生信息")
    print("\t\t\t\t\t 2.搜索学生信息")
    print("\t\t\t\t\t 3.删除学生信息")
    print("\t\t\t\t\t 4.修改学生信息")
    print("\t\t\t\t\t 5.学生信息排序")
    print("\t\t\t\t\t 6.统计学生人数")
    print("\t\t\t\t\t 7.显示学生信息")
    print("\t\t\t\t\t 0.退出系统")

def insert():
    lst = []
    s_keys = ["id", "name", "english", "python", "java"]
    while True:
        s_values = []
        s_id = input("请输入ID")
        if not s_id:
            break
        s_name = input("请输入name")
        if not s_name:
            break
        try:
            s_english = eval(input("请输入english: "))
            s_python = eval(input("请输入python: "))
            s_java = eval(input("请输入java："))
        except:
            s_english = 0
            s_python = 0
            s_java = 0
        s_values.append(s_id)
        s_values.append(s_name)
        s_values.append(s_english)
        s_values.append(s_python)
        s_values.append(s_java)
        lst.append({key.title(): value for key, value in zip(s_keys, s_values)})
        answer = input("is next y/n: ")
        if answer == "y" or answer == "Y":
            continue
        else:
            break

    save(lst)

def save(lst):
    with open(filename, "a+", encoding="utf8") as file:
        for item in lst:
            # file.write(item.__str__())
            file.write(str(item))
            file.write("\n")
        print("completed")

def delete():
    while True:
        s_id = input("请输入ID")
        if s_id != '':
            lst = get_students()
        else:
            break

        flag = False

        with open(filename, "w", encoding="utf-8") as file:
            for item in lst:
                d = dict(eval(item))
                if d["Id"] == s_id:
                    flag = True
                    continue
                else:
                    file.write(str(d) + "\n")

        if flag:
            print("delete succeed")

        answer = input("is next y/n: ")
        if answer == "y" or answer == "Y":
            continue
        else:
            break


def search():
    while True:
        s_id = input("请输入ID")
        if s_id != '':
            lst = get_students()
        else:
            print("no student info")
            break

        for item in lst:
            d = dict(eval(item))
            if d["Id"] == s_id:
                print(title)
                print(format_title.format(d["Id"], d["Name"], d["English"], d["Python"], d["Java"],
                                          d["English"] + d["Python"] + d["Java"]))
            else:
                continue
        answer = input("is next y/n: ")
        if answer == "y" or answer == "Y":
            continue
        else:
            break


def update():
    while True:
        s_id = input("请输入ID")
        if s_id != '':
            lst = get_students()
        else:
            print("no student info")
            break

        with open(filename, "w", encoding="utf-8") as file:
            for item in lst:
                d = dict(eval(item))
                if d["Id"] == s_id:
                    print("find it")
                    while True:
                        try:
                            d["Name"] = input("please input name: ")
                            d["English"] = eval(input("请输入english: "))
                            d["Python"] = eval(input("请输入python: "))
                            d["Java"] = eval(input("请输入java："))
                        except:
                            print("输入有误，请重新输入")
                        else:
                            print("update success")
                            break

                file.write(str(d) + "\n")

        answer = input("is next y/n: ")
        if answer == "y" or answer == "Y":
            continue
        else:
            break


def sort():
    lst = get_students()
    sort_by = eval(input("please select asc(0) or dec(1): "))
    if sort_by == 0:
        lst.sort(key=lambda i: eval(i)["Name"], reverse=False)
    else:
        lst.sort(reverse=True)

    # 可以增加选择输入排序的依据
    show_student(lst)

def total():
    lst = get_students()
    print("total is ", len(lst), " students")

def show():
    lst = get_students()
    show_student(lst)


def show_student(lst):
    print(title)
    for item in lst:
        d = dict(eval(item))
        print(format_title.format(d["Id"], d["Name"], d["English"], d["Python"], d["Java"],
                                  d["English"] + d["Python"] + d["Java"]))

def get_students():
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            lst = file.readlines()
    else:
        lst = []

    print(lst)
    return lst


def main():
    while True:
        start()
        try:
            choice = eval(input("请选择："))
        except NameError:
            print("请输入数字")
            continue
        if choice in range(0, 8):
            if choice == 0:
                print("sure?")
                answer = input("please input y/n")
                if answer == "y" or answer == "Y":
                    print("Thank you")
                    break
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                update()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            else:
                show()
        else:
            print("请重新选择")
            continue

if __name__ == "__main__":
    myList = ["{'Id': '2', 'Name': '3', 'English': 3, 'Python': 3, 'Java': 3}",
     "{'Id': '3', 'Name': '3', 'English': 3, 'Python': 3, 'Java': 3}",
     "{'Id': '1', 'Name': '5', 'English': 1, 'Python': 1, 'Java': 1}",
     "{'Id': '2', 'Name': '2', 'English': 2, 'Python': 2, 'Java': 2}"]
    myList.sort(key=lambda i: eval(i)["Name"], reverse=True)
    print(myList)
    myList.sort()
    main()