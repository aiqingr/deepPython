# -*- coding:utf-8 -*-
# Author: Nick

import heapq  # q => queue 优先队列
import random

li = list(range(40))
random.shuffle(li)
print(li)

heapq.heapify(li)  # 建堆 => 小根堆
for i in range(len(li)):
    print(heapq.heappop(li), end=",")  # 每次返回最小的元素

