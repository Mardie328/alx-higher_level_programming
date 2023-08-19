#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list(set(my_list))
    result = 0
    for i in range(len(unique_list)):
        result += unique_list[i]
    return result
