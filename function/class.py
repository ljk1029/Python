#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
说明文档：类的使用说明

作者： ljk
日期：2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

# 私有变量
# 实例的变量名如果以__开头，就变成了一个私有变量private，只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.score))


# 继承
# common_para 类变量共享， private_para 是私有的
# 但是change后是对实例更改，common_para 被使用后独立
class Animal(object):
    common_para = 1
    def __init__(self, name):
        self.name = name
        self.private_para = 10
    def run(self):
        print('Animal is running...')
    def change(self, com, pri):
        self.common_para = com
        self.private_para = pri
        return [self.common_para, self.private_para]
    def display(self):
        print("name:" + self.name + " com:" + str(self.common_para) + " pri:" + str(self.private_para))


class Dog(Animal):
    #def __init__(self, name):
    #   super().__init__()
    #   self.name = name
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')


def class_test():
    # 私有变量测试
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()

    # 继承测试
    dog = Dog("Dog")
    dog.run()
    print("isinstance:", isinstance(dog, Animal))
    print("type:", type(dog))

    # 共有变量测试
    animal  = Animal("Animal")
    animal_ = Animal("Animal_")
    dog.display()
    animal.display()
    animal_.display()

    # 所有值改变
    Animal.common_para = 3
    dog.display()
    animal.display()
    animal_.display()

    # 只有animal值变
    print("change:", animal.change(2, 20))
    dog.display()
    animal.display()
    animal_.display()

    # 只有animal值不变
    Animal.common_para = 4
    dog.display()
    animal.display()
    animal_.display()


#main
if __name__ == '__main__':
    class_test()