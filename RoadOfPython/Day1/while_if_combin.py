# -*- coding:utf-8 -*-
# Author: Nick

age_of_me = 30
count = 0

while count < 3:
    guess = int(input("Please guess my age: "))
    if guess < age_of_me:
        print("Think bigger")
    elif guess == age_of_me:
        print("You are right")
        break
    else:
        print("Think smaller")
    count += 1

    if count == 3:
        continue_confirm = input("Do you want to keep trying....")
        if continue_confirm != 'n':
            count = 0
