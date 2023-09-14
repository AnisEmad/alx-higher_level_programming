#!/usr/bin/python3
""" defining a append_write function"""


def append_write(filename="", text=""):
    """ append text to filename"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.append(text)
