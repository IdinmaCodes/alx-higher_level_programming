#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set()
    for i in my_list:
        unique_nums.add(i)
    return sum(unique_nums)
