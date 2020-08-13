# -*- coding:utf-8 -*-
# Author: Nick

class People:

    def __init__(self, name, role, weapon, life_value=100, money=10000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value  # 私有属性
        self.money = money

    def show_status(self):
        """
        私有属性可以通过类中的方法进行读取更改
        """
        print(f"{self.name} holds {self.weapon} with {self.__life_value}")

    def get_shot(self):
        self.__life_value -= 50
        print("Ah, I got shot")

    def buy_weapon(self, weapon):
        print(f"{self.name} bought a {weapon}")

    def __get_life(self):
        print(f"{self.name} got healed with 10 life")
        self.__life_value += 10

    def have_blood_package(self, have_package):
        if have_package is True:
            self.__get_life()


r1 = People("Nick", "police", "B44")
r1.buy_weapon("AK47")
# print(r1.__life_value) 已经无法直接得到这个私有属性了
r1.get_shot()
r1.show_status()
r1.have_blood_package(True)
r1.show_status()