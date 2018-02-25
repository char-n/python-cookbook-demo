#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 9:38

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('a.txt', '*.txt'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, '*.csv')])

# fnmatch 在windows上大小写敏感,linux上大小写不敏感,最好使用fnmatchcase

print(fnmatch('a.txt', '*.TXT'))
print(fnmatchcase('a.txt', '*.TXT'))
