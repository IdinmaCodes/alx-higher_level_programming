#!/usr/bin/python3
import add_0

def add(a, b):
    result = add_0.add(a, b)
    print("{}+{}={}".format(a, b, result))

a = 1
b = 2
add(a, b)
