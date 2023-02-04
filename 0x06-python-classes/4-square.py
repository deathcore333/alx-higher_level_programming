#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            return TypeError("size must be an integer")
        if value < 0:
            return ValueError("size must be >= 0")
        self.__size = value
