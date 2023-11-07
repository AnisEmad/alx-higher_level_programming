#!/usr/bin/python3
""" this module for load_from_json_file function """


import json


def load_from_json_file(filename):
    """ this function loads object form json file """
    with open(filename, 'r') as file:
        return json.loads(filename)