#!/usr/bin/python3
"""Creates object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates objects from JSON file"""
   with open(filename) as f: 
        return json.load(f)
