# -*- coding:utf-8 -*-
# Author: Nick

# select_sort_simple的时间复杂度就是O(n^2)
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)  # 增加了时间复杂度 O(n)
        li_new.append(min_val)
        li.remove(min_val)  # 增加了时间复杂度 O(n)
    return li_new


def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i  # 最小值是无序区的第一个
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:  # 这个不加也可以
            li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [3, 4, 2, 1, 5, 6, 8, 7, 9]
# print(select_sort_simple(li))
select_sort(li)
print(li)