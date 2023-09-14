#!/usr/bin/python3
""" defining a class_to_json function"""


def class_to_json(obj):
    """ class to json fucntion """
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, (str, int, bool)):
        return obj
    else:
        return str(obj)
