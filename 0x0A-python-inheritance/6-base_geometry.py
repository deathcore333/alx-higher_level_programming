#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Class with public instance method to raise exception"""
    def area(self):
        raise Exception("area() is not implemented")
