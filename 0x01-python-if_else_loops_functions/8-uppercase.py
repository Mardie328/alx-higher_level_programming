#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(char), end='')
    print()
