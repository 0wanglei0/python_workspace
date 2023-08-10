"""
不可变序列
字符串，元组
没有增删改操作，改变之后地址会改变
元组定义使用()

t=(value, value1, value2)  #括号可以省略， 逗号必须有
t=tuple(value, value1, value2)
只有一个元素
t=(value,)
空元组
t=()
t=tuple()

元组的目的
·在多任务环境下，同时操作对象不需要加锁

注意事项
·元组存储的是对象的引用
1.元组中对象本身是不可变对象，则不能在引用其他对象
2.元组中对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
"""
lst = [20, 30]
t=(10, lst, 40)  #1.10是不可变的，引用的lst是不可变的，lst的值是可以改变的
lst.append(50)

print(t)

"""
元组的遍历
tuple[index]
for item in tuple
"""

print(t[1])

"""
集合

内置数据结构
可变类型的序列
集合是没有value的字典
不可添加重复项
集合是无序的

创建
·直接 {item， item1， item2}
·通过set()转成集合
"""
c = {"hello"}
print(type(c))

s = set(range(5))
print(s)
print(set([1,2,3,4])) # 列表转成集合
print(set((5,6,7,8))) # 元组转成集合
print(set({8:7,6:5})) # 字典key转成集合
print(set("python"))  # 字符串拆分转成集合
print(set())          # 空集合


"""
集合的相关操作
·判断是否存在
in / not in

·新增
1.add 一次一个
2.update 一次至少一个

·删除
1.remove 删除一个指定元素，不存在抛出异常
2.discard 一次删除一个指定元素，不存在不会抛出异常
3.pop 一次删除一个任意元素
4.clear 清空集合
5.del 删除集合
"""

s = {1, 2, 3, 4}
s.add(5)
print(s)
s.update([6, 7, 8])
print(s)
s.update((9,))
print(s)

s.remove(1)
print(s)
s.discard(0)
print(s)

s.update(["test", "new", "python"])
s.pop()
print(s)

s.pop()
print(s)

s.pop()
print(s)

s.clear()
print(s)

del s
# print("result:", s)

"""
集合间关系

集合是否相等
==或!=

判断子集
·issubset
B 是A的自己
·issuperset
A 是B的超集

·isdisjoint
是否有交集, True 无交集 False 有交集
"""

s1 = {1, 2, 3}
s2 = {"new", 1, 2, 3, "python"}
s3 = {"new", 4, 5, 6, "python"}
print("s1 is subset s2： ", s1.issubset(s2))
print("s1 is issuperset s1： ", s1.issuperset(s2))
print("s2 is subset s1： ", s2.issubset(s1))
print("s2 is issuperset s1： ", s2.issuperset(s1))
print("s3 is isdisjoint s2： ", s3.isdisjoint(s2))
print("s3 is isdisjoint s1： ", s3.isdisjoint(s1))

"""
交集
intersection
&

并集
union
|

差集
difference
-

对称差集
symmetric_difference

以上都不会更改原集合
对应的_update的方法会改变原有集合
"""

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s3))
print(s1 | s3)
print(s1)

print(s2.difference(s1))
print(s1.difference(s2))
print(s2 - s2)

print("before: ", s1)
print("before: ", s2)
print(s2.symmetric_difference(s1))
print(s2.symmetric_difference_update(s1))
print("after: ", s1)
print("after: ", s2)


"""
集合生成式

{i for i in range(1, 10)}
元组没有生成式
"""

print({i for i in range(1, 10)})
print((i for i in range(1, 10))) # generator python中的generator保存的是算法


"""
总结：
数据结构      是否可变      是否可重复      是否有序      定义符号
list          可变           可            有          []
tuple         不可变         可           有          ()
dict          可变         key不可          无          {key, value}
set           可变           不可           无          ()
"""