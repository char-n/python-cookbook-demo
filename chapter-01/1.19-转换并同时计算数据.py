#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/24 20:50

# 计算平方和
nums = [1, 2, 3, 4, 5]
# 以前的做法

my_nums = []
for x in nums:
    my_nums.append(x * x)

print(sum(my_nums))

# 现在的做法(使用了生成器)
print(sum(x * x for x in nums))

# 显示的传递一个生成器
sum((x * x for x in nums))
