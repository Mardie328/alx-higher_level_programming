#!/usr/bin/python3
for number in range(100):
    if (number >= 0 and number <= 98):
        print("{}{}, ".format((number // 10), number % 10), end="")
    else:
        print("{}{}".format((number // 10), number % 10))
