#!/usr/bin/python3
""" defining a mylist class"""


class MyList(list):
    """ class MyList """
    def print_sorted(self):
        print(sorted(self))
