# -*- coding:utf-8 -*-
# Author: Nick
class Dog(object):
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print(f"{self.name} is bulking")

    def __call__(self, *args, **kwargs):
        print("runing call", args, kwargs)

    def __str__(self):  # Django 时候就会使用了
        return f"<obj: {self.name}>"


# print(Dog.__dict__)  # 打印类的属性 不包括实例的属性
d = Dog("xixi")
# print(d.__dict__)  # 打印实例的属性不包括类的属性
print(d)