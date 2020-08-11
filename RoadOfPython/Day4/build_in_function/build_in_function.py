# -*- coding:utf-8 -*-
# Author: Nick
print(abs(-1))  # 绝对值
print(all([1, -2, 3, 4, 0]))  # 返回True 当可迭代对象里所有元素都为True
print(any([1, -2, 3, 4, 0]))  # 返回True 当可迭代对象里 至少有一个元素为True
print(any([]))
print(bin(2))  # 数字转换成二进制
print(chr(90))  # unicode to char
print(ord("z"))  # char to unicode
# res = filter(lambda x: x > 5, range(10))
# for i in res:
#     print(i)
#
# res = map(lambda n: n*n, range(10))
# for i in res:
#     print(i)

print(round(1.123, 2))
print(round(1.451, 1))

a = [1, 5, 6, 2, 7]
b = {
    1: 5,
    12: 3,
    11: 123,
    19: 21,
    2: 4567
}
# print(sorted(a))
# print(sorted(b.items()))
# print(sorted(b.items(), key=lambda x: x[1]))
x = [111, 2]
y = ["a", "b", "c"]
for i in zip(x, y):
    print(i)
