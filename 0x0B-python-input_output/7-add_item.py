#!/usr/bin/python3
"""
script that adds all arguments a python list
and save it to a json file

"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arg_count = len(sys.argv)
try:
    list = load_from_json_file("add_item.json")
except FileNotFoundError:
    list = list()

for i in range(1, arg_count):
    list.append(sys.argv[i])

save_to_json_file(list, "add_item.json")
