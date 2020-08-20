# -*- coding:utf-8 -*-
# Author: Nick
import random


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]
    for var in li:
        i = min(var // (max_num//n), n-1)  # i 表示var放进几号桶里 10000//100 = 100 但是只有0-99 一百个桶
        buckets[i].append(var)  # 把var加入桶里面
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


li = [random.randint(0,10000) for i in range(10000)]
li = bucket_sort(li)
print(li)
