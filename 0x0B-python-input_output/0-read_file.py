#!/usr/bin/python3
""" this module for read_file function """


def read_file(filename=""):
    """ this function reads a file and print it"""
    with open(filename, 'r') as f:
        file = f.read()
        print(file, end="")
