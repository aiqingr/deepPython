# -*- coding:utf-8 -*-
# Author: Nick

# 这种修改文件的方法是找到需要修改的地方 然后把所有的写入一个新的文件
f = open("original_file", "r")
f_new = open("changed_file", "w")
for line in f:
    if "This is my 9 line." in line:
        line = line.replace("This is my 9 line.", "I changed this line content. You can not find digit 9 any more.")
    f_new.write(line)
f.close()
f_new.close()