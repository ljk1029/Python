#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime

# 文件打开
def file_open(path):
    f = open(path, 'a+')
    f.write('Hello, world!')
    f.seek(0)
    print(f.read())
    f.close()

# 路径添加
def path_add():
    sys.path.append('..')
    print("path:", sys.path)

# 路径设置
def os_demo():
    print('name:',  os.name)
    print('uname:', os.uname)
    print('environ:',  os.environ)
    print('environ:',  os.environ.get('PATH'))
    path = os.path.abspath('.')
    print("path:", path)
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    dir_path = os.path.join(path, 'testdir')
    print("dir_path:", dir_path)
    # 然后创建一个目录:
    os.mkdir(dir_path)
    # 删掉一个目录:
    os.rmdir(dir_path)

#命令行参数
def sys_demo():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def time_demo():
    now = datetime.now() # 获取当前 datetime
    print(now)

# main
if __name__ == '__main__':
    path = 'test.txt'
    file_open(path)
    path_add()
    os_demo()
    sys_demo()
    time_demo()
    