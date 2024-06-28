#!/usr/bin/python3
"""
Module: json_to_object
Converts a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Converts JSON string to Python object.
    """
    return json.loads(my_str)
