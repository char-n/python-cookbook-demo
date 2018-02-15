#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/15 12:46

from collections import OrderedDict

# 控制字典中元素的顺序

o = OrderedDict()
o['foo'] = 1
o['bar'] = 2
o['spam'] = 3
o['gork'] = 4
o['gork'] = 5

for key, value in o.items():
    print(key, value)

# 精确控制json编码之后元素的顺序
import json

dumps = json.dumps(o)
print(dumps)

# 注意事项:一个OrderedDict的大小是普通字典的两倍.内部维护着另外一个链表,使用的时候要权衡利弊
