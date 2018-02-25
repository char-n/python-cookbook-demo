#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 11:21

import re

text1 = 'Computer says "no."'

re_compile = re.compile(r'\"(.*)\"')
findall = re_compile.findall(text1)
print(findall)

text2 = 'Computer says "no." Phone says "yes."'
print(re_compile.findall(text2))

# 非贪婪模式匹配
re_compile = re.compile(r'\"(.*?)\"')
print(re_compile.findall(text2))
