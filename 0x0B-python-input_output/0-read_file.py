#!/usr/bin/python3
""" defining read_file function"""


def read_file(filename=""):
    """ reads filename with utf-8 encoding"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
