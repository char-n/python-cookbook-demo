#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/19 12:03

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

row_by_fname = sorted(rows, key=itemgetter('fname'))
print(row_by_fname)

# 多个key排序
row_by_uid_and_fname = sorted(rows, key=itemgetter('uid', 'fname'))
print(row_by_uid_and_fname)

# 该技术同样适用于min(),max()
row_min = min(rows, key=itemgetter('uid'))
print(row_min)
