# -*- coding:utf-8 -*-
# Author: Nick

def insert_sort(li):
    for i in range(1, len(li)):  # i 标示摸到牌的下标
        tmp = li[i]
        j = i -1  # j 指的是当前手里的最右侧的牌的下标（手里最大牌的下标）
        while li[j] > tmp and j >= 0:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)


li = [3, 2, 4, 1, 6, 7, 8, 9]
insert_sort(li)
print(li)