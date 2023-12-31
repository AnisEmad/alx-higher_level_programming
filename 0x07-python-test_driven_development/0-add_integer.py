#!/usr/bin/python3
""" this is add_integer module """


def add_integer(a, b=98):
    """ this function add two numbers and return it's sum """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
