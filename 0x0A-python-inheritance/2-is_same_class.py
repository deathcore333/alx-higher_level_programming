#!/usr/bin/python3
"""function that checks an object's instance"""


def is_same_class(obj, a_class):
    """Checks if an object is the instance of a class
    Args:
        obj: the object to check
        a_class: class to check against
    Returns:
        True if object is instance of a class
    """
    return type(obj) is a_class
