#!/usr/bin/python3
""" this module for append_write function """


def append_write(filename="", text=""):
    with open(filename, 'a') as file:
        return file.write(text)
