# -*- coding:utf-8 -*-
# Author: Nick

class Dog(object):
    n = "asd"

    def __init__(self, name):
        self.name = name
        self.__age = 23

    @staticmethod  # 静态方法 实际上和类没有什么关系了 但是需要通过类调用
    def eat(self, food):  # 可以去掉self 如果这个函数不需要引用self里的变量
        print(f"{self.name} is eating {food}")

    @classmethod
    def sleep(cls):
        print(f"{cls.n} is sleeping at")

    @property
    def walk(self):
        print(f"{self.name} is walking")

    @walk.setter
    def walk(self, distance):
        print(f"{self.__age} years old walk {distance} miles")

    @walk.deleter
    def walk(self):
        del self.__age
        # print(self.__age)
        print("deleted")


d = Dog("xixi")
Dog.eat(d, "baozi")  # 通过这个方式来调用staticmethod
Dog.sleep()
d.walk = 10
del d.walk  # 属性方法无法直接用del删除 需要加入deleter
