#!/usr/bin/python3
""" defining a write file function"""


def write_file(filename="", text=""):
    """ write text to filename"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
