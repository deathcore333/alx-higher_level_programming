#!/usr/bin/python3
"""Inserts a line of text to a file after each line with a certain str"""


def append_after(filename="", search_string="", new_string=""):
    """
    Add a line of text to file after each line with a
    specific string.
    Args:
        filename (str): name of the file
        search_string (str): the string to search
        new_string (str): string to add
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
