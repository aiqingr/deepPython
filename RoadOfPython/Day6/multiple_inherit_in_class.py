# -*- coding:utf-8 -*-
# Author: Nick
class A(object):
    def __init__(self, name):
        self.name = name
        print("A")


class B(A):
    def __init__(self, name):
        self.name = name
        print("B")


class C(A):
    def __init__(self, name):
        self.name = name
        print("C")


# 多继承的情况下 D里面没有构造函数的情况下 就先找B 再找C 最后再找A 就是所谓的广度优先
# python3 里都是广度优先（无论是经典类 还是新式类） python2里经典类是深度优先 先找B 再找A 最后找C 而新式类是按照广度优先继承
class DD(B, C):

    def new_func(self):
        print("123")


obj = DD("nick")
obj.new_func()

