#!/usr/bin/python3
"""Returns the object from JSON serialization"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure"""
    return obj.__dict__
