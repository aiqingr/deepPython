# -*- coding:utf-8 -*-
# Author: Nick
class Role:
    n = 123  # 类变量
    name = "This is my name"
    class_of_list = []
    class_of_dict = {
        "No1": 1,
        "No2": 2
    }

    def __init__(self, name, role, weapon, life_value=100, money=10000):
        """
        构造函数
        在实例化时做一些类的初始化工作
        """
        self.name = name  # 实例变量（静态属性） 作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def got_shot(self):  # 类的方法（也就是功能）=> 动态属性
        print("ah, I got shot")

    def buy_gun(self, gun_name):
        print(f"{self.name} just bought {gun_name}")


print(Role)
r1 = Role("Nick", "police", "B22")  # 实例化（初始化一个类 造 了一个对象）
r2 = Role("Yang", "terrorist", "AK47")  # 把一个类变成一个具体对象的过程叫 实例化（初始化）
r1.buy_gun("B32")
# r1 = Role(r1, "name", "police", "weapon") # 这也是为什么要有self在__init__
# 类的方法 并不存储在实例的内存地址中 所以每一个类的方法都有一个self
# r1.got_shot() => Role.got_shot(r1)
print(r1.n, r1.name)  # 先找实例变量 再找类变量
r1.name = "BigNick"
print(r1.name)
r1.bullet_proof = True
print(r1.bullet_proof)
r1.n = "hahaha"  # 相当于在r1内存地址创建了一个名为n的实例变量 所以在print的时候 先找了实例变量
print(r1.n)
print(r2.n)  # 但在r2中并没有名为n的实例变量 所以只能找到类变量 类变量是原值
Role.n = "woyougaile"
print(r1.n, r2.n)
r1.class_of_list.append("myR1")
r2.class_of_list.append("FromR222222")
print(f"Role => {Role.class_of_list}\nR1 => {r1.class_of_list}\nR2 => {r2.class_of_list}")
# 类里的list改变了数值 是因为在类中的list是一个内存地址 在更改的时候 指向的内存地址的list改变了
# 和单纯的类变量 不同 dict对应的原理相同
r1.class_of_dict["No2"] = 5
r2.class_of_dict["No3"] = "newDictContent"
print(f"""
Role => {Role.class_of_dict}
R1 => {r1.class_of_dict}
R2 => {r2.class_of_dict}
""")



