#!/usr/bin/python3
"""
JSON file operations.
"""

import json


def load_from_json_file(filename):
    """
    Load JSON from file.
    """
    with open(filename, encoding='UTF8') as f:
        return json.load(f)
