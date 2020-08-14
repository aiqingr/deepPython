# -*- coding:utf-8 -*-
# Author: Nick
# -*- coding:utf-8 -*-
# Author: Nick
# class People: 经典类
class People(object):  # 新式类 不同主要体现在多继承上
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def talk(self):
        print(f"{self.name} is talking")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Relation(object):
    # 见inherit_in_class_more
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(f"{self.name}")

    def make_friends(self, obj):
        print(f"{self.name} is making friend with {obj.name}")
        # self.name 继承了People 所以这个object已经有name这个属性了


class Man(Relation, People):  # 继承了People这个类
    # 现有的代码报错 是因为 Man不具有自己的初始化 那么就会寻找第一个父类的初始化
    # 所以Man这个类中就不具有People的name这个属性了
    def piao(self):
        print(f"{self.name} is piaoing")

    def sleep(self):
        People.sleep(self)
        print(f"{self.name} is sleeping with a girl")


class Woman(People):

    def give_birth(self):
        print(f"{self.name} born a baby")


people1 = Man("Nick", 23)
people1.eat()
people1.piao()
people1.sleep()
woman1 = Woman("Jia", 22)
woman1.give_birth()
people1.make_friends(woman1)