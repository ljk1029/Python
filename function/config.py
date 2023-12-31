#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
说明文档：第三方库，配置解析

作者： ljk
日期:  2024/01/01

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

# json用法
import json
def json_demo():
    d = dict(name='Bob', age=20, score=88)
    print(json.dumps(d))
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str))

# base64用法
import base64
def base64_demo():
    L = b'binary\x00string'
    A = base64.b64encode(L)
    Q = b'YmluYXJ5AHN0cmluZw=='
    B = base64.b64decode(Q)
    print("enbsse64:", L, A)
    print("debsse64:", Q, B)

# 数据哈希用法
import hashlib
def hash_demo():
    L = 'how to use md5 in python hashlib?'
    print("hash:", L)
    
    md5 = hashlib.md5()
    md5.update(L.encode('utf-8'))
    print("md5:", md5.hexdigest())

    sha1 = hashlib.sha1()
    sha1.update(L.encode('utf-8'))
    print("sha1:", sha1.hexdigest())

if __name__ == '__main__':
    json_demo()
    base64_demo()
    hash_demo()