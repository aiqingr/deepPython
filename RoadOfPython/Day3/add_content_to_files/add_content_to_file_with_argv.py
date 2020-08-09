# -*- coding:utf-8 -*-
# Author: Nick
"""
f = open("original_file_2", "w")
for i in range(10):
    f.write(f"This is my {i} line. \n")

f.close()
"""
import sys

find_str = sys.argv[1]
change_str = sys.argv[2]

f1 = open("original_file_2", "r")
f2 = open("changed_file_2", "w")

for line in f1:
    if "This is my 6 line." == find_str:
        line = line.replace(find_str, change_str)
    f2.write(line)

f1.close()
f2.close()
