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

import base64
def base64_test():
    L = b'binary\x00string'
    A = base64.b64encode(L)
    Q = b'YmluYXJ5AHN0cmluZw=='
    B = base64.b64decode(Q)
    print("enbsse64:", L, A)
    print("debsse64:", Q, B)


import hashlib
def hash_test():
    L = 'how to use md5 in python hashlib?'
    print("hash:", L)
    md5 = hashlib.md5()
    md5.update(L.encode('utf-8'))
    print("md5", md5.hexdigest())

    sha1 = hashlib.sha1()
    sha1.update(L.encode('utf-8'))
    print("sha1", sha1.hexdigest())

if __name__ == '__main__':
    open_test('/home/ljk/hgfs.link/VMCode/github/B_python/function/test.txt')
    json_test()
    base64_test()
    hash_test()