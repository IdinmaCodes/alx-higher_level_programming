#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sorted_keys = sorted(keys)
    for i in sorted_keys:
        value = a_dictionary[i]
        print(f"{i}: {value}")
