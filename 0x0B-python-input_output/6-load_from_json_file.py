#!/usr/bin/python3
"""load from json"""
import json


def load_from_json_file(filename):
    """load from json to file"""
    with open(filename, encoding="utf-8") as file_loaded:
        return json.load(file+loaded)
