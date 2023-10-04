#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#if
def if_test( number ):
    age = number
    if age >= 18:
        print(age, 'adult')
    elif age >= 6:
        print(age, 'teenager')
    else:
        print(age, 'kid')


#for
def for_test():
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
    
    sum = 0
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        sum = sum + x
    print(sum)

#while
def while_test():
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)

#input
def input_test():
    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
        print('00 前')
    else:
        print('00 后')



if __name__ == '__main__':
    if_test(3)
    for_test()
    while_test()
    input_test()