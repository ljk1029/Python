#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
说明文档：解析输入参数

作者： ljk
日期：2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

import argparse

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logPath", required=True, help="Specify the log file.")
    parser.add_argument("--o", help="Specify the output path for the file.")
    args = parser.parse_args()
    return args

# 使用示例
args = parse_input()
print("Log file path:", args.logPath)
print("Output file path:", args.o)