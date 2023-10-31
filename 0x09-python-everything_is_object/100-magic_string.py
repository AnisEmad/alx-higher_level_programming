#!/usr/bin/python3
def magic_string():
    if not hasattr(magic_string, "n"): magic_string.n = 0; magic_string+= 1
    return magic_string.n * "BestSchool"
