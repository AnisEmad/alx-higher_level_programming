#!/usr/bin/python3
import json


""" defining a to_json_string function"""


def to_json_string(my_obj):
    """ returns a json representation of an object"""
    json_string = json.dumps(my_obj)
    return json_string
