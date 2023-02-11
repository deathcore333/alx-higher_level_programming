#!/usr/bin/python3
"""Writes a string in a text file as JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to textfile using JSON representation
    Arg:
        my_obj (str): Object to add to text file
        filename (str): name of the file to add the JSON
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
