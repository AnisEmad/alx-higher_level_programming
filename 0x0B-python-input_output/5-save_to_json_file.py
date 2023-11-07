#!/usr/bin/python3
""" this module for save_to_json_file function """


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    file = json.dumps(my_obj)

    with open(filename, 'w') as f:
        f.write(file)
