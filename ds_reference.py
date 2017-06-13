#!/bin/python
#coding: utf-8
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist只是指向同一对象的另一种名称
mylist = shoplist

# 购买了第一项，所以我将其从列表中删除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 这个时候打印出的两个列表都没有apple，说明这两个列表指向的是同一个对象

print('Copy by making a full slice')
# 生成一份完整的切片,制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 这个时候两个列表内容不相同