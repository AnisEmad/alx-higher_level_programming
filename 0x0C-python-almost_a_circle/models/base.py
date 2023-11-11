#!/usr/bin/python3
""" this module for base class """


class Base:
    """ this is a class base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
