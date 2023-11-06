#!/usr/bin/python3
""" this module for rectangel class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class Rectangle that inherit from BaseGeometry"""
    def __init__(self, width, height):
        Rectangle.integer_validator("width", width)
        Rectangle.integer_validator("height", height)
        self.__width = width
        self.__height = height
