#!/usr/bin/python3
def no_c(my_string):
    i = len(my_string) - 1
    for i in range(i, -1, -1):
        if my_string[i].lower() != 'c':
            print("{}".format(my_string[i]))
