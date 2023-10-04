#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def trys_test():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
        print('END')

import logging
# 设置日志等级
logging.basicConfig(level=logging.INFO)
def log_test():
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)

#main
if __name__ == '__main__':
    trys_test()
    log_test()