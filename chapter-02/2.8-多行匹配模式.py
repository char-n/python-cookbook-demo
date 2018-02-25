#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 11:24

text1 = '/* this is a comment */'
text2 = '''/* this is a
 multiline comment */
 '''

import re

re_compile = re.compile(r'/\*(.*?)\*/')
print(re_compile.findall(text1))
print(re_compile.findall(text2))

# 匹配多行方式一:
re_compile = re.compile(r'/\*((?:.|\n)*?)\*/')
print(re_compile.findall(text2))

# 匹配多行方式二:
re_compile = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(re_compile.findall(text2))
