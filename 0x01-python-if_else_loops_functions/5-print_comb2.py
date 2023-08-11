#!/usr/bin/python3
for number in range(100):
    if (number >= 0 and number <= 99):
        print("{}{}, ".format((number // 10), number % 10))
    else:
        print("{}{}, ".format(int(number / 10), number % 10), end="")
