#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a print module '

__author__ = 'ljk'

# list可变对象
#
#



# print
def print_test():
    print("hello, python")
    print('您好!, python')
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print('中文'.encode('gb2312'))
    print(len('ABC'))


#list
def list_test():
    classmates = ['Michael', 'Bob', 'Tracy']
    print("list:", classmates)
    print("list pop():", classmates.pop())
    print("list pop(1):", classmates.pop(1))
    print("list:", classmates)
    print("list:", list(range(5)))
    a = ['c', 'b', 'a', 'a']
    print("list:", a)
    a.sort()
    print("list:", a)


#tuple 不能修改一旦初始化
def tuple_test():
    classmates = ('Michael', 'Bob', 'Tracy')
    print("tuple:", classmates)
    #防止只有一个元素，歧义
    t = (1,)
    print("tuple:", t)


#dict
def dict_test():
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print("dict:", d)
    print("dict:", d['Michael'])
    #add
    d['Adam'] = 67  
    print("dict:", d['Adam'])
    #exist
    print("dict: Thomas is exist in d:", 'Thomas' in d)
    #pop
    print("dict:", d.pop('Bob'))
    print("dict:", d)
    return d


#set 元素不能重复
def set_test():
    s = set([1, 1, 2, 2, 3, 3])
    print("set:", s)
    s.add(4)
    print("set:", s)
    s.remove(3)
    print("set:", s)


#str
def str_test():
    a = 'abc'
    print("str:", a)
    print("str:", a.replace('a', 'A'))
    print("str:", a)
    print("str: ABC", 'ABC'.lower())
    return a   


#math
def math_test():
    a = abs(-20)
    print("adb:", a)
    b = max(2, 3, 1, -5)
    print("max:", b)


#type
def type_test():
    print("type:", int('123')) 
    print("type:", int(12.34))
    print("type:", float('12.34'))
    print("type:", str(1.23))
    print("type:", str(100))
    print("type:", bool(1))
    print("type:", bool(''))


# 默认值指向可变对象
def add_end_a(L=[]):
    L.append('END')
    return L

# 默认值指向不可变对象
def add_end_b(L=None):
    if L is None:
        L = []
        L.append('END')
    return L

#命令行参数
import sys
def sys_test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

import os
def os_test():
    print('name:',  os.name)
    print('uname:', os.uname)
    print('environ:',  os.environ)
    print('environ:',  os.environ.get('PATH'))
    #os.path.abspath('.')
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    #os.path.join('/Users/michael', 'testdir')
    # 然后创建一个目录:
    #os.mkdir('/Users/michael/testdir')
    # 删掉一个目录:
    #os.rmdir('/Users/michael/testdir')

from datetime import datetime
def time_test():
    now = datetime.now() # 获取当前 datetime
    print(now)

# main
if __name__ == '__main__':
    print_test()
    list_test()
    tuple_test()
    dict_test()
    set_test()
    str_test()
    math_test()
    type_test()
    print(add_end_a())
    print(add_end_a())
    print(add_end_b())
    print(add_end_b())
    sys_test()
    os_test()
    time_test()
    pass