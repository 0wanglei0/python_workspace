from itertools import zip_longest

list1 = [1, 2, 3, 4, 5]
# list1 = [1, 2, 2]
list2 = [2, 4]
# list2 = [2, 4, 6, 8]

# 此处转换会舍弃多余的key或value，只有对应匹配有值的才能对应到字典上
a = dict(zip(list1, list2))
print(a)

# 此处如果key长度大于value长度会报错，没有更多的value赋值给key，抛出异常
# b = {key: list2[i] for i, key in enumerate(list1)}
# print(b)

# 此方法会将未对应的key或value设置为None，key唯一，value不唯一，可都为None
c = {k: v for k, v in zip_longest(list1, list2)}
print(c)
#
# for item in list2:
#     if item in list1:
#         list1.remove(item)
#
# print(list1)
#
# string = "message"
# s_dict = {}
# for s in string[:]:
#     if s in s_dict.keys():
#         s_dict[s] += 1
#         continue
#     s_dict[s] = 1
# print(s_dict)

# netstat -an 查看系统占用端口
