#!/usr/bin/python3
""" this module for from_json_string function """


import json


def from_json_string(my_str):
    """ this function returns an object form string json representation """
    return json.loads(my_str)
