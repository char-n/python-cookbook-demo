#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/19 19:38

# 最简单的过滤序列元素的方法就是使用列表推导
mylist = [1, 2, 3, 4, 5]
print([n for n in mylist if n > 3])

# 适用列表的缺陷是如果输入非常大会占用很大的内存

# 适用生成器
pos = (n for n in mylist if n > 3)
for n in pos:
    print(n)

# 过滤规则比较复杂
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


iterator = filter(is_int, values)
print(iterator)
print(list(iterator))

# 列表在过滤的时候转换数据
print([x * x for x in mylist if x > 2])

# 将不符合条件的值用新值替代
print([n if n > 2 else 0 for n in mylist])
