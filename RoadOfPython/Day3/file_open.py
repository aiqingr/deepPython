# -*- coding:utf-8 -*-
# Author: Nick
# f = open("my_file1", "w")
# for i in range(10):
#     print(f"{i} \n")

# f = open("my_file1", "a")
# f.write("When I was young")

# f = open("my_file1", "r")
# for i in range(6):
#     print(f.readline().strip())

f = open("my_file1", "a")
"""
第二种循环 用到了迭代器
count = 0
for line in f:
    if count == 6:
        print("********")
        count += 1
        continue
    count += 1
    print(line.strip())
"""

"""
第一种循环
for index, line in enumerate(f.readlines()):
    if index == 6:
        print("**********")
        continue
    print(line.strip())
"""
print(f.tell())
# print("**********")
# f.readline()
# print(f.tell())
# print("**********")
# f.readline()
# print(f.tell())
# print("**********")
# f.readline()
# print(f.tell())
# print("**********")
# print(f.seek(2))
print(f.encoding)
print(f.name)
# print(f.fileno())
print(f.flush())  # 强行写入硬盘 完成后在进行下一步
f.seek(10)
f.truncate(10)  # seek移动的光标和截断的光标是相互独立的 所以尽管移动光标到十 但还是只截断
# 最开始的是个characters
f.close()
