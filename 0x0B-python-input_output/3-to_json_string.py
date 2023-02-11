#!/usr/bin/python3
"""Defines a JSON-converting function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of string object"""
    return json.dumps(my_obj)
