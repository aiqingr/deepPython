# -*- coding:utf-8 -*-
# Author: Nick

import sys

print("**************")
print(sys.path)  # 打印环境变量
for i in range(len(sys.path)):
    print(sys.path[i])
print("##############")
#
print(sys.argv)  # 打印参数
print(sys.argv[0])  # 当运行 python3 sys_module.py a b c // a b c 也会当做参数被打印出来


