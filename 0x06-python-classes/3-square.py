#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            return TypeError("size must be an integer")
        if size < 0:
            return ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
