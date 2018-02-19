#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/19 12:10

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(2), User(3)]
from operator import attrgetter

sort_by_user_id = sorted(users, key=attrgetter('user_id'))
print(sort_by_user_id)
