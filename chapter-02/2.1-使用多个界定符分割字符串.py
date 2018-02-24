#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/24 21:15

# 你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。

line = 'asdf fjdk; afed, fjek,asdf, foo'

# 使用正则
import re

split = re.split(r'[;,\s]\s*', line)
print(split)

# 注意正则中是否包含一个括号捕获分组
# 此时会把分隔符也包含进来
re_split = re.split(r'(;|,|\s)\s*', line)
print(re_split)

# 解决办法
split = re.split(r'(?:;|,|\s)\s*',line)
print(split)
