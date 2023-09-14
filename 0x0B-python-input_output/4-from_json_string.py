#!/usr/bin/python3
""" defining a from_json_string function"""


import json


def from_json_string(my_str):
    """ returns a proper data structure represented by json string"""
    data = json.loads(my_str)
    return data
