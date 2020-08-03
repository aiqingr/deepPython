# -*- coding:utf-8 -*-
# Author: Nick

import os

cmd_res = os.system("cd")  # 执行命令 但不保存结果
# print("--> cmd_res", cmd_res)

cmd_res_1 = os.popen("pwd").read()  # popen执行结果被暂时存入ram当中 需要用read方法去读取
cmd_res_2 = os.popen("pwd")
print("--> cmd_res_1", cmd_res_1)
print("--> cmd_res_2", cmd_res_2)

os.mkdir("new_dir")  # 在当前目录下 创建一个目录
