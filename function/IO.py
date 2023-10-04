#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def open_test(path):
    pass
    f = open(path, 'a+')
    f.write('Hello, world!')
    f.seek(0)
    print(f.read())
    f.close()

import json
def json_test():
    d = dict(name='Bob', age=20, score=88)
    print(json.dumps(d))
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str))


if __name__ == '__main__':
    open_test('/home/ljk/hgfs.link/VMCode/github/B_python/function/test.txt')
    json_test()