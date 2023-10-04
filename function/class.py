#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#实例的变量名如果以__开头，就变成了一个私有变量private，只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.score))





#继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')



def test():
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()

    dog = Dog()
    dog.run()
    print("isinstance:", isinstance(dog, Animal))
    print("type:", type(dog))

#main
if __name__ == '__main__':
    test()