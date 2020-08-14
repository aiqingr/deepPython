# -*- coding:utf-8 -*-
# Author: Nick
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):  # 这个就是在实现多态化
        obj.talk()


class Dog(Animal):
    def talk(self):
        print("Woof Woof")


class Cat(Animal):
    def talk(self):
        print("Miao")


dog1 = Dog("haha")
cat1 = Cat("xixi")
Animal.animal_talk(dog1)
Animal.animal_talk(cat1)