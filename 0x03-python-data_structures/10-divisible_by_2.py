#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    new_list = []
    for i in range(length):
        if (my_list[i] % 2 == 0):
            divisible_number = True
        else:
            divisible_number = False
        new_list.append(divisible_number)
    return new_list
