#!/bin/python
# coding: utf-8
zoo = ('python', 'elephant', 'penguin')
print('Nomber of animals in the zoo is', len(zoo))      #获取元组的长度

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])       #通过索引访问new_zoo中的第三个元素
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))        #通过索引访问new_zoo中第三个
                                                                                        #元素的第三个元素