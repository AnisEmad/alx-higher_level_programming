#!/usr/bin/python3
""" defining a to_json_string function"""


import json


def to_json_string(my_obj):
    """ returns a json representation of an object"""
    json_string = json.dumps(my_obj)
    return json_string
