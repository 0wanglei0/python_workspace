"""
字典

python内置的数据结构之一，是可变序列
键值对的方式存储数据，是无序序列
类似map，用key查value

"""

# 创建字典方式1 {}

scores = {"a": 10, "b": 20, "c": 30}
print(scores)

# 创建字典方式2 dict
score = dict({"a": 20, "b": "30", "c": 30.1})
print(score)

#字典获取数据方式1 dict[key] 此方式当key不存在时会抛出异常
print(scores["a"])

#字典获取数据方式2 get(key) 此方式当key不存在时返回None，get()也可以提供默认值 get(key, default)
print(score.get("b"))
print(score.get("d", 73))

"""
key的判断
in/not in

清空
dict.clear()

删除
del dict[key]

新增
dict[key]=value

获取字典视图的三个方法
keys()  获取所有key
values() 获取所有value
items() 获取所有key，value键值对

字典元素遍历

for key in dict

总结：
·字典的所有元素都是一个键值对，key不允许重复，value可以
·字典的元素是无序的
·key是不可变对象
·字典也可动态变化
·字典浪费内存，空间换时间的数据结构
"""

print(type(score.values()))
print(list(score.items())[0])
print(list(score.items())[0].__getitem__(0))

## key是不可变的，“3”被保存为key了，即使a变了，dict保存的key还是“3”
a = "3"
## lst = list(["a", "b"])
## score[lst] = "b"  list是可变的，不能作为key   报错：TypeError: unhashable type: 'list'
score["$a"] = "b"
a = "4"
print(score.get(a))

"""
字典生成式

dict = {key：value, key1: value}

"""

keys = ["aa", "bb", "cc"]
values = [1, 2, 3, 4, 5]

# zip()方式  默认以短的进行赋值, zip之后是对象，需要转换才能使用
d = { key1.title(): value1 for key1, value1 in zip(keys, values)}
print(d)

print(zip(keys, values))

# 迭代器
some_dict = {'a': 1, 'b': 2, 'c': 3}
print(some_dict)
dict_iter = iter(some_dict)
print(next(dict_iter))

for i in dict_iter:
    print(i)

# 生成器
"""
生成器是一种计算机制，一边循环一边计算
"""

# 列表推导式
L = [x * x for x in range(5)]
print(L)

# 生成器
G = (x * x for x in range(5))
print(G)

# 调用生成器的第一种方式
next(G)

# 第二种方式 是for循环