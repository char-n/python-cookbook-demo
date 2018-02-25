#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 9:33

import os

listdir = os.listdir('.')
print(listdir)

# 检查多种匹配可能.需要将所有的匹配放到一个元组中
print([name for name in listdir if name.endswith(('.py', '.c'))])
