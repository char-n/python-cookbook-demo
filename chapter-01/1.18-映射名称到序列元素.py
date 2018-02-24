#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/24 20:28

# 命名元组
from collections import namedtuple

MyTuple = namedtuple('MyTuple', ['name', 'age'])
my_tuple = MyTuple('niuzhifa', '100')
print(my_tuple)

# 支持所有的普通元组操作
# 索引
print(len(my_tuple))
# 解压
name, age = my_tuple
print(name, age)

# 如果要改变命名元组的属性.需要使用_replace方法,会创建一个全新的元组,并把相应的字段用新的值替换
replace = my_tuple._replace(name='zhangsan')
print(replace)
print(my_tuple)
