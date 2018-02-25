#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/25 10:54

text = 'UPPER PYTHON, lower python, Mixed Python'
import re

findall = re.findall('python', text, flags=re.IGNORECASE)
print(findall)

sub = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(sub)


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        if text.islower():
            return word.lower()
        if text[0].isupper:
            return word.capitalize()
        else:
            return word

    return replace


re_sub = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(re_sub)
