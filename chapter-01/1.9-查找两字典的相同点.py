#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/15 17:36

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 12
}

# 查找相同的键
print(a.keys() & b.keys())

# 查找在a而不在b中的键
print(a.keys() - b.keys())

# 查找公共的键值对
# 没有达到效果??
print(a.items() & b.items())

# 过滤字典
c = {key: a[key] for key in a.keys() - {'z'}}
print(c)
