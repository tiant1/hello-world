#!/bin/python
# _*_ conding: utf-8 _*_
import os
import time
source = ['"C:\\My Documents"', 'D:\\mypython']

target_dir = 'E:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)  == 0:
    print('Successful backup to', target)
else:
    print('Backup Failed')