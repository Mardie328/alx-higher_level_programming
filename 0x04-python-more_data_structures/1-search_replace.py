#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    for i in range(len(new_list)):
        if (new_list[i] == search):
            new_list[i] = replace
    return new_list
