#!/usr/bin/python3
"""a function that prints a square with the hash char"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == type(float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
