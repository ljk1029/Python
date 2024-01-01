#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a thread module '

__author__ = 'ljk'

from multiprocessing import Pool
import os, time, random
import threading




# 大量进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# 进程池创建
def pool_demo():
    print('Parent process %s.' % os.getpid())
    # 创建一个包含4个进程的进程池
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 子进程创建
def fork_demo():
    print('Process (%s) start...' % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 线程函数
def thread_fun():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s exit.' % threading.current_thread().name)

# 线程创建
def thread_demo():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=thread_fun, name='LoopThread')
    t.start()
    t.join()
    print('thread %s exit.' % threading.current_thread().name)


if __name__ == '__main__':
    # 放到前面防止多进程，导致多线程
    thread_demo() 
    fork_demo()
    pool_demo()
    