# -*- coding:utf-8 -*-
# Author: Nick

# set 去重 关系测试
list_1 = [1, 12345, 3, 5, 6, 87, 2, 2, 3, 5, 6]
list_1 = set(list_1)  # 集合是无序的 作用去重
print(list_1, type(list_1))
list_2 = [1, 4, 56, 6, 2, 7, 123]
list_2 = set(list_2)

list_intersection = list_1.intersection(list_2)  # 关系测试 取交集
print(list_intersection)

list_union = list_1.union(list_2)
print(list_union)  # 关系测试 取并集
list_diff = list_1.difference(list_2)
print(list_diff)  # in list_1 but not in the list_2
list_3 = set([3, 5])
print(list_1.issubset(list_3))
print(list_1.issuperset(list_3))

list_symmetric = list_1.symmetric_difference(list_2)
print(list_symmetric)  # 取非交集的剩余元素

list_4 = set([1, 2, 3, 4])
list_5 = set([1, 2, 4, 5])

print(list_4 & list_5)  # union
print(list_4 | list_5)  # intersection
print(list_4 - list_5)  # difference
print(list_4 ^ list_5)  # symmetric

set_1 = set("asdqweaaa")
print(set_1)
set_1.add("a")  # add one item to set
print(set_1)
set_1.update(["1", "qwe", "a", 123])  # add multiple items to set
print(set_1)
set_1.remove(123)
print(set_1)
print(len(set_1))

for i in set_1:
    print(i)
print("************")
print(set_1.pop())  # arbitrary item
set_2 = set([1, 2, 3, "ad"])
set_2.discard("ad")  # 区别于remove 当item 不在集合中的时候 discard并不会报错 remove会报错
print(set_2)
