#!/usr/bin/python3
"""Reads the text file(utf-8) and prints to stdout"""


def read_file(filename=""):
    """
    This function reads the contents of the file and prints
    Args:
        filename (str): filename
    Return:
        Nothing
    """
    with open('filename', r, encoding='UTF-8') as f:
        print(f.read(), end="")
