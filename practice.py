#!/usr/bin/python3

class Person:
    def __init__(self, name):
        self.name = name


    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Mwas')
p.say_hi
