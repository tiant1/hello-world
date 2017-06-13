#!/bin/python
# coding: utf-8
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or "subscription' operation #
# 索引或下标操作符（Subcription）“操作符”
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])       #索引操作作用负数表示从最末尾开始计数，倒数第1计为-1
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list，对列表进行切片
print('Item 1 to 3 is', shoplist[1:3])     #索引中的数字第一个表示切片开始的位置，第二个表示切片结束的位置
                                                #如果第一个数字省略表示从第一个元素开始切片，第二个数字省略表示
                                                # 切片至最后一个数字
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

#从某一字符串中切片
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

print(shoplist[::2])

list = [0, 1, 2, 3, 4, 5, 6, 7]
print(list[1:5:2])
print(list[::-1])