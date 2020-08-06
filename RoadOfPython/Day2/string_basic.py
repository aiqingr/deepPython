# -*- coding:utf-8 -*-
# Author: Nick
name = "my name is Nick HHHHHHHHH"
test_name = "my name is {name}, my age is {age}"
print(name.count("h"))  # case sensitive
print(name.capitalize())  # cap first letter
print(name.center(50, "-"))
print(name.endswith("Nick"))  # return boolean value
print(name.find("name"))
print(name[name.find("name"): 10])
print(test_name.format(name="Nick", age=23))
print("13231".isdigit())
print("1.0".isdecimal())  # return false since . is a special character
print(name.join("---"))
print("+".join(["1", "2", "3"]))
print(name.rjust(40, "*"))  # ljust
print(name.lower())
print(name.upper())
print("  Nick   ".strip())  # rstrip and lstrip
p = str.maketrans("abcdefg", "1234567")
print("Ni Tongyang abc".translate(p))  # p就是一个简单的编码
print("Nick Ni".replace("i", "O", 1))
# print("alex li".rfind("o"))
print("1+2+3+4".split("+"))
print("1+2+3".split())