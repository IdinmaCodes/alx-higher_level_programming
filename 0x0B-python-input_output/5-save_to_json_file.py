#!/usr/bin/python3
"""
Module: save_to_json_file
Function that writes object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    """
    with open(filename, 'w', encoding='UTF8') as f:
        json.dump(my_obj, f)
