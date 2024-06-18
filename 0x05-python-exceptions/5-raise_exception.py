#!/usr/bin/python3

def raise_exception():
    try:
        raise_exception()
    except TypeError as e:
        print("TypeError raised as expected.")
