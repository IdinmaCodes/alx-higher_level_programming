#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if isinstance(i, int):
                print("{:d}".format(i))
                count += 1
    except Exception as e:
        print(f"An error occurred: {e}")
    return count
