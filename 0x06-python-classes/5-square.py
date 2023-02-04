#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        """Return the area of the current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the area with the # character."""
        if size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """Get/set the size of the current square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            return TypeError("size must be an integer")
        if value < 0:
            return ValueError("size must be >= 0")
        self.__size = value
