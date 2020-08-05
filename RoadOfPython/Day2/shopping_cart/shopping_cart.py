# -*- coding:utf-8 -*-
# Author: Nick
shopping_list = [
    ("IPhone", 7000),
    ("Mac Pro", 20000),
    ("Car Model LOGO", 300),
    ("Concert Ticket", 1000),
    ("PS5", 3000)
]
print(shopping_list)
# quit_app_action = True
my_salary = int(input("Please enter you salary: "))
my_shopping_cart = []
my_remain_salary = my_salary
while my_remain_salary:
    selection = input("Please select your item ")
    if selection == "q":
        print(f"Your balance is {my_remain_salary}.")
        exit()
    else:
        my_selection = int(selection)
        my_remain_salary = my_remain_salary - shopping_list[my_selection-1][1]
        if my_remain_salary > 0:
            my_shopping_cart.append(shopping_list[my_selection-1])
            print(f"{shopping_list[my_selection-1][0]} is added to your cart. And your balance is {my_remain_salary}.")
        else:
            print("You don't have enough balance")
            print(f"Your shopping cart is {my_shopping_cart}")
            my_remain_salary = my_remain_salary + shopping_list[my_selection - 1][1]
            print(f"Your balance is {my_remain_salary}.")
            continue


