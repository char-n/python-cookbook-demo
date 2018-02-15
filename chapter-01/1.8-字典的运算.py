#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/15 12:55

# 如何在字典中求最大值,最小值和排序
# 思路:对字典的键和值进行反转.

prices = {
    'AA': 12,
    'BB': 23,
    'CC': 34
}

iterator = zip(prices.values(), prices.keys())
for key, value in iterator:
    print(key, value)

iterator = zip(prices.values(), prices.keys())
print(min(iterator))

iterator = zip(prices.values(), prices.keys())
print(max(iterator))

# 注意:zip创建的是一个只能访问一次的迭代

# 如果字典中的元素的值相同,那么拥有最大或最小的键的实体会返回
prices = {
    'AA': 23,
    'CC': 23,
}

print(max(zip(prices.values(), prices.keys())))
print(min(zip(prices.values(), prices.keys())))
