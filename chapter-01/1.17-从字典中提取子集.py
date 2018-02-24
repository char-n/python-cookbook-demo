#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/24 20:11

# 使用字典推导的方法
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

new_price = {key: value for key, value in prices.items() if value > 20}
print(new_price)

teach_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# {}不仅仅代表字典?
teach_names = ['AAPL', 'IBM', 'HPQ', 'MSFT']
p2 = {key: value for key, value in prices.items() if key in teach_names}
print(p2)

# 也可以实现.但是比字典推导慢
p3 = dict((key, value) for key, value in prices.items() if value > 20)
print(p3)