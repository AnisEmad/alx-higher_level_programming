#!/usr/bin/python3
""" this module is for student class"""


class student:
    """ calss student with attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
