# -*- coding:utf-8 -*-
# Author: Nick
shopping_list = [
    ("IPhone", 6000),
    ("Mac Pro", 19000),
    ("Music Ticket", 1000),
    ("LOGO", 500),
    ("Apple Watch", 7000)
]
shopping_cart = []
my_salary = input("Please enter your salary: ")
if my_salary.isdigit():
    salary = int(my_salary)
    while True:
        for index, val in enumerate(shopping_list):
            print(index, val)
        user_choice = input("选择买的物品： ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if len(shopping_list) > user_choice >= 0:
                p_item = shopping_list[user_choice]
                if p_item[1] <= salary:  # be able to afford
                    shopping_cart.append(p_item)
                    salary -= p_item[1]
                    print(f"Added {p_item[0]} into shopping cart, your current balance is {salary}")
                else:
                    print(f"Your current balance is {salary}. You are not able to afford it.")
            else:
                print("Your selection is not in shopping list.")
        elif user_choice == "q":
            for i in shopping_cart:
                print(i)
            exit("Thx")
        else:
            print("Invalid input")
else:
    print("You didn't enter your salary")