#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 9:47

text1 = '11/27/2012'

import re

re_compile = re.compile(r'\d+/\d+/\d+')
match = re_compile.match(text1)
print(match.group())

findall = re_compile.findall(text1)
print(findall)

# 使用分组
# 使用原始字符串可以不用解析反斜杠

re_compile = re.compile(r'(\d+)/(\d+)/(\d+)')
compile_match = re_compile.match(text1)
print(compile_match.group(0))
print(compile_match.group(1))
print(compile_match.group(2))
print(compile_match.groups())

# 注意.match()只是匹配开始部分.如果需要精确匹配.确保正则表达式已$结尾
text2 = '12/23/2014kkkl'
print('====')
re_compile = re.compile(r'(\d+)/(\d+)/(\d+)$')
if re_compile.match(text2):
    print(re_compile.match(text2).group(0))
