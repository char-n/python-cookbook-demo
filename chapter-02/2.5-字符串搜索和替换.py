#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 10:44

# 简单的字符串替换可以使用str.replace()方法
text = 'yeah, but no, but yeah, but no, but yeah'
replace = text.replace('yeah', 'yep')
print(text)
print(replace)

# 复杂的模式可以使用re模块中的sub()函数
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# 将11/27/2012 的日期字符串改成 2012-11-27
import re

sub = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(sub)
