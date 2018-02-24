#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/24 21:01

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

# 大部分字典的操作都可以使用
print(len(c))
print(list(c.keys()))

# 如果键出现重复,第一次出现的映射值会返回
# 对于字典的更新或删除操作总是影响的是列表中第一个字典
c['x'] = 23
print(a)
print(c)
