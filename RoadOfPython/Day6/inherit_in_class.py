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
    # def __init__(self, n1, n2):
    #     self.n1 = n1
    #     self.n2 = n2
    #     print(f"{self.name}")

    def make_friends(self, obj):
        print(f"{self.name} is making friend with {obj.name}")
        # self.name 继承了People 所以这个object已经有name这个属性了


class Man(People, Relation):  # 继承了People这个类

    def __init__(self, name, age, money):  # 当子类 需要更多的参数输入的时候 需要重构init 必须加入父类的参数
        # People.__init__(self, name, age)  两种方法继承父类 第二种可能稍好 尤其是在多继承的情况下
        super(Man, self).__init__(name, age)  # super 是新式类的写法
        self.money = money
        print("money")

    def piao(self):
        print(f"{self.name} is piaoing")

    def sleep(self):
        People.sleep(self)
        print(f"{self.name} is sleeping with a girl")


class Woman(People):

    def give_birth(self):
        print(f"{self.name} born a baby")


people1 = Man("Nick", 23, 100)
people1.eat()
people1.piao()
people1.sleep()
woman1 = Woman("Jia", 22)
woman1.give_birth()
people1.make_friends(woman1)