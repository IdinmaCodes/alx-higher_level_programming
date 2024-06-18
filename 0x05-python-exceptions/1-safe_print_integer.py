#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}\n".format(value))
        return True
    except Exception as e:
        print("An error occurred: {}\n".format(e))
        return False
