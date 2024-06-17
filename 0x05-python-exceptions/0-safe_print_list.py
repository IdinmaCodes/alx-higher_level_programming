#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints the first x elements of a list and returns the number of elements printed.
    
    Args:
        my_list (list): The list to print from.
        x (int): The number of elements to print.
    
    Returns:
        int: The number of elements printed.
    """
    counter = 0
    if x > len(my_list):
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
