#!/usr/bin/python3
""" this module for is_same_class function"""


def is_same_class(obj, a_class):
    """
    True if the object is exactly
    an instance of the specified class ;
    otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
