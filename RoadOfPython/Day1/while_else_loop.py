# -*- coding:utf-8 -*-
# Author: Nick

age_of_me = 30
count = 0
while count < 3:
    age = int(input("Guess his age: "))
    if age < age_of_me:
        print("Think bigger")
    elif age == age_of_me:
        print("You guess right")
        break
    else:
        print("Think smaller")
    count += 1
else:  # while 语句当中可以增加else语法
    print("You have tried too many times. F*ck off")