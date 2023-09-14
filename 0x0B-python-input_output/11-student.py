#!/usr/bin/python3
""" this module is for student class"""


class Student:
    """ calss student with attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            data = self.__dict__
            new = dict()
            for str in attrs:
                for key, value in data.items():
                    if key == str:
                        new[key] = value
            return new
    def reload_from_json(self, json):
        self.__dict__ = json
