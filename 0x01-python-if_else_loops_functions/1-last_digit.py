#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    print("Last digit of {:d} is -{:d} and is less than 6 and not 0".format(number, last_digit))
elif number == 0:
    print("Last digit of {:d} is 0".format(number))
elif number > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
