#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
