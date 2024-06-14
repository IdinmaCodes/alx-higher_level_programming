#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    combined = set()  # Initialize an empty set
    for i in set_1:
        if i not in set_2:
            combined.add(i)
    for i in set_2:
        if i not in set_1:
            combined.add(i)
    return combined
