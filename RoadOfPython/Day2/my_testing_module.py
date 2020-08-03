# -*- coding:utf-8 -*-
# Author: Nick

import getpass
username = "nick"
password = "123"
username_1 = input("username: ")
password_1 = getpass.getpass("password: ")
if username_1 == username and password_1 == password:
    print(username_1, password_1)
else:
    print("Invalid user")
