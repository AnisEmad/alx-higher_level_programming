#!/usr/bin/python3
""" this module for class Mylist """


class MyList(list):
    """ this class inherit from list class """
    def print_sorted(self):
        """ prints a list in sorted way """
        print(sorted(self))
