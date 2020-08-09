# -*- coding:utf-8 -*-
# Author: Nick
# with syntax can help us close file automatically
with open("with_open_file_1", "r") as f, \
        open("with_open_file_2", "r") as f2:  # 这种打开多个文件的方式 可以帮助减少每一行的代码数量 官方推荐每一行代码少于80
    for line in f:
        print(line)