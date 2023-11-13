#!/usr/bin/python3
""" this module for base class """


import json


class Base:
    """ this is a class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_dictionary(self):
        """ to dictonary function """
        pass

    @staticmethod
    def to_json_string(list_dictionaries):
        """ this convert list of dicts to a json string """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ this saves a list of objs to a file """
        if list_objs is None:
            data = "[]"

        else:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            data = cls.to_json_string(list_dictionaries)
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """ this convert json string to an object """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ this function creates an instance with attriubtes """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ this function loads a list of obj from a file """
        try:
            filename = f"{cls.__name__}.json"
            with open(filename, 'r') as file:
                json_data = file.read()
            list = cls.from_json_string(json_data)
            new_list = []
            for dict in list:
                new_item = cls.create(**dict)
                new_list.append(new_item)
            return new_list
        except FileNotFoundError:
            return []
