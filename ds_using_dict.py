#!/bin/python
#coding: utf-8
# “ab”是地址簿（Address Book）的缩写
ab = {
    'Swaroop' : 'swaroop@swaroopch.com',
    'Larry' : 'larry@wall.org',
    'Matusmoto' : 'matz@ruby-lang.org',
    'Spammer' : 'spammer@hotmail.com',
}

print("Swaroop's address is", ab['Swaroop'])

#删除一对键值对
del ab['Spammer']


print('\nThere are {} contacts in the address book'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
