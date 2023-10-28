#!/usr/bin/python3
""" this is a moudle for indentation"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for chr in text:
        print(chr,end="")
        if chr == '.' or chr == '?' or chr == ':':
            print('\n')
