#!/usr/bin/python3
""" this module for add attr func """


def add_attribute(obj, attr, value):
    """ add atrribute to object if possiable """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
