#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            print()
            return True
        else:
            print("Error: value is not an integer")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
