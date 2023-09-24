#!/usr/bin/python3
"""Defines a function that appends a string at the end of a
text file(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added

    Args:
        filename (str): filename to append
        text (str): text to append
    Returns: 
        the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
