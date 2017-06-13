#!/bin/python
# coding: utf-8
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa".')

if 'a' in name:
    print('Yes, it contains the string "a".')

if name.find('war') != -1:
    print('Yes, it contains the string "war".')

# 给列表加进特定的字符串
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
