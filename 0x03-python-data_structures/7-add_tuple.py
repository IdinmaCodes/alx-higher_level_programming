#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        return None

    first_a = tuple_a[0]
    first_b = tuple_b[0]
    sum1 = first_a + first_b

    second_a = tuple_a[1]
    second_b = tuple_b[1]
    sum2 = second_a + second_b

    return sum1, sum2
