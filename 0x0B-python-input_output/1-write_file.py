#!/usr/bin/python3
""" this module for write_file function """


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        return f.write(text)
