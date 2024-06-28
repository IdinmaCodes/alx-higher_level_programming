#!/usr/bin/python3
"""
Module: json_representation
Provides a function to return the JSON string of an object.
"""

import json


def to_json_string(my_obj):
    """
    Returns JSON string of an object.
    """
    return json.dumps(my_obj)
