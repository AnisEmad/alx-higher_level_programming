#!/usr/bin/python3
""" this module for load_from_json_file function """


import json


def load_from_json_file(filename):
    """ this function loads object form json file """
    with open(filename, 'r') as file:
            json_data = json.load(file)
            return json_data
