#!/usr/bin/python3
"""Defines an inherited list class Mylist"""


class MyList(list):
    """implements sorted printing for the builtin list class."""

    def print_sorted(self):
        """Prints the sorted list."""

        print(sorted(self))
