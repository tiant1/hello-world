#!/bin/python
# coding: utf-8
import os
import time

# 需要备份的文件与目录放到一个列表中
# 在Windows下
source = ['"C:\\My Documents"', 'D:\\mypython']
# 在Linux下
# source = ['/usr/etc/', '/usr/local/etc']

# 备份文件的存储位置
# 在Windows下
target_dir = 'E:\\Backup'
# 在Linux下
# target_dir = /Backup

# 备份文件的名称
target = target_dir + os.sep + \
        time.strftime('%Y%m%d%H%M%S') + '.zip'
# 如果目标目录不存在则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)        #调用系统指定创建目录

# 压缩命令
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')