#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

from PIL import Image

def path_test():
    sys.path.append('..')
    print("path:", sys.path)
    

def pillow_test():
    im = Image.open('test.png')
    print(im.format, im.size, im.mode)  
    im.thumbnail((200, 100))
    im.save('thumb.jpg', 'JPEG')




# main
if __name__ == '__main__':
    path_test()
    pillow_test()