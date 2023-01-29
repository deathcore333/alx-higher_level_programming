#!/usr/bin/python3
def uppercase(string):
    for i in range(string):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            print("{}".format(chr(ord(string[i]) - 32)), end="")
    print("\n")
