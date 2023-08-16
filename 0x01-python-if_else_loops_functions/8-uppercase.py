#!/usr/bin/python3
def uppercase(str):
    modified_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            modified_str += chr(ord(char) - 32)
        else:
            modified_str += char

    print(modified_str, end='\n')
    print()  
    return modified_str  
