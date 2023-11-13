#!/usr/bin/python3
""" this module for base class """


import json


class Base:
    """ this is a class base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_dictionary(self):
        pass

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            data = []
        
        filename = f"{cls.__name__}.json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        data = cls.to_json_string(list_dictionaries)
        
        with open(filename, 'w') as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy    
