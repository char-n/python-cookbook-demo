# encoding=utf-8
from collections import deque

# 解压序列赋值给多个变量

'''
1.任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多
个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的
'''

# 元组
p = (2, 3)
x, y = p

print(x)
print(y)

# 列表
data = ['username', 'password', 25]
username, password, age = data
print(username)
print(password)
print(age)

# 字符串
s = 'hello'
a, b, c, d, e = s
print(a, b, c, d, e)

# 解压部分变量,使用任意变量名去替换
data = ['username', 'password', 25]
username, _, age = data
print(username, age)

'''
2. 变量的数量必须跟序列元素的数量不一样,使用*号表达式
'''
record = ['niuzhifa', '123', 'read', 'basketball']
# *号表达式解压出来的是列表类型.即使序列中只有0个元素
# *号表达式也可以用在列表的开始部分
username, password, *hobby = record
print(username, password, hobby)

# *号表达式在迭代元素为可变长元组的序列的应用
records = [
    ('foo', 1, 2),
    ('bar', 5),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if 'foo' == tag:
        do_foo(*args)
    if 'bar' == tag:
        do_bar(*args)

# *号表达式在字符串的应用
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)

# 解压元素之后丢弃
record = ('name', 12, 34, (2, 4, 1990))
name, *_, (*_, year) = record
print(name, year)

# 递归 ???
items = [1, 2, 3, 4, 5]


def sum(items):
    head, *tail = items
    # 这一行代码如何理解
    return head + sum(tail) if tail else head



print(sum(items))


# 长度为3的队列
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)

print(d)

d.append(4)

# d.pop()
d.popleft()

print(d)

# 无限长的队列
d = deque()
d.append(1)
d.append(2)
d.append(3)

print(d)

d.appendleft(0)
print(d)