#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 11:38

s = ' hello world \n'

rstrip = s.rstrip()
print(rstrip)

lstrip = s.lstrip()
print(lstrip)

strip = s.strip()
print(strip)

s = '--hello world ===='
s_lstrip = s.lstrip('-')
print(s_lstrip)

print(s.rstrip('='))
print(s.strip())

s = 'hello     world'
print(s.replace(' ', ''))

import re
print(re.sub('\s+', ' ', s))
