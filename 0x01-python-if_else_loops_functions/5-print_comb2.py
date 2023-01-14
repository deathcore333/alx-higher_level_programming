#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print(num)
    print("{}".format('0' + str(num) if num < 10 else num), end=", ")
