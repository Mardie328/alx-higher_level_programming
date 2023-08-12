#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        new_str = ""
        for i in range(len(str)):
            if i != n:
                new_str += str[i]
        return new_str
    else:
        return str
