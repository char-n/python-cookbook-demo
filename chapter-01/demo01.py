# encoding=utf-8

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
