#!/usr/bin/python3
"""
Defines a function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string

    Args:
        my_str: A JSON string
    
    Returns: Python data structure 
    """
    return json.loads(my_str)