#!/usr/bin/python3
""" this module for my_int class """


class MyInt(int):
    """ calss myint that inherit from int """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
