#!/usr/bin/python3
""" this module for add_item script """


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


args = sys.argv
list = args[1:]
try:
    load = load_from_json_file("add_item.json")
    list = load + list
except Exception:
    pass
save_to_json_file(list, "add_item.json")
