#!/usr/bin/python3
"""Checks if object is instance of or if the object
is instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): object to check
        a_class (type): class to match the obj
    Returns:
        if object is exactly instance of a_class - True.
        False otherwise
    """
    return isinstance(obj, a_class)
