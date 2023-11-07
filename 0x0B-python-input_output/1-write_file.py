#!/usr/bin/python3
""" this module for write_file function """


def write_file(filename="", text=""):
    """ this function write to a file and return the number of bytes written"""
    with open(filename, 'w') as f:
        return f.write(text)
