#!/usr/bin/python3
for number in range(100):
    if (((number // 10) != number % 10) and ((number // 10) < number % 10)):
        if number == 89:  # Last number in the loop
            print("{}{}".format((number // 10), number % 10), end=" ")
        else:
            print("{}{}".format((number // 10), number % 10), end=", ")
print()
