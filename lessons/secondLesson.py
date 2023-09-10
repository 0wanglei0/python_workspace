"""
列表：相当于其他语言中的数字

·可以存放不同类型的数据

·列表的特点：
 1.元素有序
 2.索引映射唯一数据 list[0],可以使用负数，倒序索引
 3.可以存储重复数据
 4.存放不同类型数据
 5.根据需要动态分配和回收内存

·列表查询
1.list.index() 获取当前元素的索引,存在重复数据，返回第一个元素
可以在指定范围内查找

2.获取列表中的单个元素
list[index]
索引不正确会抛出异常

3.获取列表多个元素：切片
list[start : stop : step]
默认start=0， stop=max step=1,不包含stop
值都可为空

step=负数，默认start为最后一个元素

·判断是否为列表元素
元素 in/not in list

·列表元素增加
  1.append 末尾添加元素
  2.extend 末尾至少添加一个元素
  3.insert 任意位置插入一个元素
  4.切片 任意位置添加至少一个元素
"""

# 第一种创建list的方式
lst1 = ["hello", "world", 95]

print(id(lst1)) #id是引用地址
print(type(lst1)) #类型
print(lst1) #输出

#第二种创建list的方式,使用内置函数list

lst = list(["hello", "world too", 98])
print(lst.index("hello", 0, 3))
print(lst[0 : 1])
print(lst[0 : -1])
print(lst[2 : : -1])

lst.append("python") # 如果此处添加的是列表，用append会将列表作为一个元素插入
lst.extend(lst1) # 会将列表元素拆分插入
lst.insert(1, "lalalalala")
print(lst)

lst[7:] = lst1 #切换
print(lst)


"""
列表移出

remove 移出元素
pop 移出索引位置元素，默认最后一个
切片
clear 清空列表
del 删除列表 使用此方法， 再使用时会抛出异常报错
"""

lst.remove(98)
lst.pop(2)
result = lst.pop()
lst[1:3]=[] #切片方式

"""
修改列表的值

一次修改一个值
list[index]=value

切片
list[start:stop]=[value, value]

"""

lst[1:3] = [10, 20]
print(lst)

"""
列表排序:数组类型相同

sort 默认从小到大，指定reverse=True，从大到小
sorted 内置函数，默认从小到大，指定reverse=True，从大到小，原列表不变,产生新的list
"""
lst = [10, 30, 40, 20, 60, 30]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
print(sorted(lst))
print(sorted(lst, reverse=True))

"""
列表生成式

[i for i in range(1, 10)]
"""

lst2 = [i for i in range(1, 10)]
print(lst2)
