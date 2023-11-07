#!/usr/bin/python3
""" this module for append_write function """


def append_write(filename="", text=""):
    """ this function append text to a file and creates one if it doesn't exist """
    with open(filename, 'a') as file:
        return file.write(text)
