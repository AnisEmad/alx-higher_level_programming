#!/usr/bin/python3
""" defining a is_same_class function """


def is_same_class(obj, a_class):
    """ is same class function """
    if isinstance(obj, a_class):
        return True
    else:
        return False
