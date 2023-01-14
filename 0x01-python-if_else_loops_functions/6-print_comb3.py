#!/usr/bin/python3
for num in range(100):
    if int(num / 10) != num % 10 and int(num / 10) < num % 10:
        print("{}{}".format(int(num / 10), num % 10), end="")
        if (num != 89):
            print(", ", end="")
print("")
