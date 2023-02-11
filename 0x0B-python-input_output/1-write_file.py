#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Writes a text into a file
    Args:
        filename (str): file name
        text (str): string to append to file
    Return:
        number of chars written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
