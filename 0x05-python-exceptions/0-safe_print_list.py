#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    if x == 0:
        return counter
    for i in my_list:
        try:
            print(i, end='')
            counter += 1
            if counter >= x:
                break
        except Exception as e:
            print(f"An error occurred: {e}")
    print()
    return counter
