# -*- coding:utf-8 -*-
# Author: Nick

# for loop 选择性输出在某些情况下不需要用if再去判定打印条件 如下：
print("********************")
for i in range(10):
    print(i)
print("--------------------")
for i in range(0,10,2):
    print(i)
print("#####################")
for i in range(0,10,3):
    print(i)