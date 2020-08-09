# -*- coding:utf-8 -*-
# Author: Nick

# 读写
f = open("complete_operating_files", "r+", encoding="utf-8")
f.readline()
print(f.tell())
f.readline()
print(f.tell())
f.readline()
print(f.tell())
f.seek(19)
print(f.tell())
f.write("---------dia-----------")  # 修改 其实是覆盖

"""
写读
f = open("complete_operating_files", "w+", encoding="utf-8")
"""
f.close()