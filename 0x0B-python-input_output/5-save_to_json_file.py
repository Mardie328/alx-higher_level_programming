#!/usr/bin/python3
"""
Defines a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Returns a JSON representation of the object in the given filename

    Args:
        my_obj: Object to write to a file
        filename: Text file name
    Returns: JSON representation of the object
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
