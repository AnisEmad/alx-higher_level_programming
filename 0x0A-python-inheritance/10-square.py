#!/usr/bin/python3
""" this module for square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class that inherit from rectangle """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
