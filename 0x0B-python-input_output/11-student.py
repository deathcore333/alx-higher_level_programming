#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents a class student"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student class
        Args:
            first_name (str): student's first name
            last_name (str): students last name
            age (int) : Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self attrs=None):
        """Get Dict representation of Student.
        if attrs is a list of strings, represents only
        attrs in this list
        Args:
            attrs (list): (Optional) attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all atttributesof the student
        Args:
            json (dict): The key/value pairs to replace attributes with
        """
        for k, v in json.items():
            setattr(self, k, v)
