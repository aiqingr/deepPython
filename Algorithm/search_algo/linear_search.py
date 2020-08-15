# -*- coding:utf-8 -*-
# Author: Nick

def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


print(linear_search([1,2,3,4,45,5,67,8,0], 8))
