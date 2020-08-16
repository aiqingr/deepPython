# -*- coding:utf-8 -*-
# Author: Nick

import random


def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:  # ">"就是升序 "<"就是升序
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return


# li = [random.randint(0, 100) for i in range(10)]
li = [9,8,7,1,2,3,4,5,6]
print(li)
bubble_sort(li)
print(li)