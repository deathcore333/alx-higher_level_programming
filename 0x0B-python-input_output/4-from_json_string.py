#!/usr/bin/python3
"""Defines a function that converts json to string"""
import json


def from_json_string(my_str):
    """Converts JSON representation to string"""
    return json.loads(my_str)
