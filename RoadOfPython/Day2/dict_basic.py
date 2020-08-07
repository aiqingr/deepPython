# -*- coding:utf-8 -*-
# Author: Nick

# dict is disorder and all its key must be unique
info = {
    "av1101": "sanshangyouya",
    "av1102": "henanlimei",
    "av1103": "Julia",
    "av1104": "qiaobenyoucai"
}

b = {
    1: 2,
    2: 3,
    "av1104": "qiaobenyoucai 2"
}

print(info["av1101"])
info["av1102"] = "shuililai"
info["av1105"] = "songdaofeng"
print(info)
del info["av1105"]
info.pop("av1103")
print(info)
print(info.get("av1103"))  # 一般用这种方法去得到一个value 以确保如果没有这个key的情况下并不会报错
print("av1101" in info)

mul_info = {
    "USA": {
        "USA1": "USA value one",
        "USA2": "USA value two",
        "USA3": "USA value three"
    },
    "CHN": {
        "CHN1": "CHN value one",
        "CHN2": "CHN value two",
        "CHN3": "CHN value three",
    }
}

print(mul_info)
mul_info["USA"]["USA1"] = "I have changed this value"
print(mul_info)
mul_info.setdefault("wojia", {"wojia1": "wojia1", "wojia2": "wojia2"})
print(mul_info)
info.update(b)
print(info)

# fromkeys 的原理有点像是copy 后面赋值的value是在ram中的一个地址 所以修改的时候 所有key的value都会跟着改变
c = dict.fromkeys([1, 7, 8], [1, {"name": "Nick"}, 2])
print(c)
c[1][1]["name"] = "Nick Ni"
print(c)

info_index = {
    "abc": "ABC123",
    "cvb": "CVB22",
    "qwe": "KJH545"
}
#  这种循环方式 是最建议的方式
for i in info_index:
    print(i, info_index[i])
# 形式上 这两种循环都是一样的 但是第一种比第二种要高效
for i, k in info_index.items():
    print(i, k)

