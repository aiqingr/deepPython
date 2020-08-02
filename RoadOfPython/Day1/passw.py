# -*- coding:utf-8 -*-
# Author: Nick
import getpass


username = input("username: ")
password = input("password: ")

print(username, password)
# getpass 这个build in的库可以帮助你隐藏输入的密码，pycharm内部的terminal不支持，另开一个terminal
username_1 = input("username: ")
password_1 = getpass.getpass("password: ")
print(username_1, password_1)