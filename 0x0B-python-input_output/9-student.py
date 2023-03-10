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

    def to_json(self):
        """Get Dict representation of Student"""
        return self.__dict__
