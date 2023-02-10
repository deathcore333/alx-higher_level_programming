#!/usr/bin/python3
"""Defines a Locked class"""


class LockedClass:
    """
    Prevent user from instantiating new LockedClass attributes
    for anything but first_name
    """
    __slots__ = ["first_name"]
