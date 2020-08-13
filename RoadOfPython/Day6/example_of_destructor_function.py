# -*- coding:utf-8 -*-
# Author: Nick

class Cat:
    def __init__(self, name, sex, age, lovely):
        self.name = name
        self.sex = sex
        self.age = age
        self.lovely = lovely

    def __del__(self):
        """
        这个是析构函数 destructor
        """
        print(f"I sell my little {self.name}")

    def food_for_it(self):
        print(f"Come on, my litter {self.name}")

    def toy_for_it(self, toy):
        print(f"I would like to buy {toy} for my little {self.name}")


cat_1 = Cat("jiajia", "female", 3, True)
cat_1.toy_for_it("AA")
del cat_1  # 实例销毁 所以在给cat_2 toy_for_it之前就可以看到 I sell ... 如果删除就在程序结束才可以看到也就是
# 现有两个buy toy 才有第一个sell
cat_2 = Cat("xiaoqing", "male", 2, False)
cat_2.toy_for_it("BB")
