# -*- coding:utf-8 -*-
# Author: Nick
data = {
    "北京": {
        "朝阳": {
            "沙河1": ["oldboy1", "test1"],
            "天通苑1": ["恋家1", "我爱我家1"]
             },
        "昌平": {
            "沙河2": ["oldboy2", "test2"],
            "天通苑2": ["恋家2", "我爱我家2"]
             },
        "海淀": {
            "沙河3": ["oldboy3", "test3"],
            "天通苑3": ["恋家3", "我爱我家3"]
             }
    },
    "上海": {
        "朝阳1": {
            "沙河11": ["oldboy11", "test11"],
            "天通苑11": ["恋家11", "我爱我家11"]
             },
        "昌平1": {
            "沙河22": ["oldboy22", "test22"],
            "天通苑22": ["恋家22", "我爱我家22"]
             },
        "海淀1": {
            "沙河33": ["oldboy33", "test33"],
            "天通苑33": ["恋家33", "我爱我家33"]
             }
    }
}

while True:
    for i1 in data:
        print(i1)

    choice1 = input("Enter your choice >>: ")  # beijing
    if choice1 in data:
        while True:
            for i2 in data[choice1]:
                print("\t", i2)

            choice2 = input("Enter your choice >>: ")  # chaoyang
            if choice2 in data[choice1]:
                while True:
                    for i3 in data[choice1][choice2]:
                        print("\t\t", i3)
