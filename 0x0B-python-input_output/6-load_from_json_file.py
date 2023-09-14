#!/usr/bin/python3
""" defining a load_from_json_file function"""


import json


def load_from_json_file(filename):
    """ loads from json file"""
    with open(filename, mode='r') as file:
        data = json.load(file)
    return data
