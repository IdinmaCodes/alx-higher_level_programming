#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    length = len(sentence)
    my_tuple = (length, first_char)
    return my_tuple
