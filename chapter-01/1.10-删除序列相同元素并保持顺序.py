#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/16 11:45

# 生成器:列表元素按照某种算法推算出来,这种一遍循环一遍推算的机制,叫做生成器
# 创建生成器,只需要把列表生成式的[]改为()
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
# 打印生成器的元素
for i in g:
    print(i)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    print('done')


# fib(6)


# 把斐波拉契数列改为生成器
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    print('done')


f = fib2(6)
print(f)

for x in fib2(6):
    print(x)
