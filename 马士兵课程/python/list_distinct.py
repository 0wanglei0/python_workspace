list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]

for item in list2:
    if item in list1:
        list1.remove(item)

print(list1)


string = "message"
s_dict = {}
for s in string[:]:
    if s in s_dict.keys():
        s_dict[s] += 1
        continue
    s_dict[s] = 1
print(s_dict)