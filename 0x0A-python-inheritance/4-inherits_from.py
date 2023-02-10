#!/usr/bin/python3
"""Defines an object/class checking function"""


def inherits_from(obj, a_class):
    """checks if object is an instance of a class that inherited from
    specified class
    Args:
        obj (any): object to check
        a_class: the class to check
    Return:
        True if it is an instance
        False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
