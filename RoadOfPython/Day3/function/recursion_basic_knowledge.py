# -*- coding:utf-8 -*-
# Author: Nick
# 递归的特性
# 1 必须有一个明确的结束条件
# 2 每次进入下一层递归的时 问题规模相比上一次都应有所减少
# 3 递归的效率不高 递归层数过多时会导致栈溢出
# 在计算机中 函数的调用是通过栈stack这种数据结构实现的 每当进入下一个函数调用的时候
# 栈就会增加一层帧 每当函数返回的时候 栈就会减少一层帧
# 由于栈的大小不是无限的 所以递归层数过多的时候 就会导致栈溢出

# def calc(n):
#     print(n)
#     if n+1 > 0:
#         return calc(n+1)
#
#
# calc(0)

def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
    print(f"The last n is {n}")


calc(20)
