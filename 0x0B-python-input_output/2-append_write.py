#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """"
    Function that appends string at the end of file
    Args:
        filename (str): name of file to append to
        text (str): string to append to file
    Return:
        Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
