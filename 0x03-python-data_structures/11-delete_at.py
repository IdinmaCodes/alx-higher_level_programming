#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list):
        return my_list
    new_list = []
    for i in my_list:
        if i != idx:  # fixed the condition to check if i is not equal to idx
            new_list.append(i)
    return new_list
