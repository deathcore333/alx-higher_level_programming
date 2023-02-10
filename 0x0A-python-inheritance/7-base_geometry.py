#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Class with public instance method to raise exception
    and another to validate integer"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
