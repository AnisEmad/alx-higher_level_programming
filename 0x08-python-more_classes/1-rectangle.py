#!/usr/bin/python3
"""
This is module defines a rectangle class
"""


class Rectangle:
    """
    A class to represent rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance
        
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: width of the rectangle"""
        return self.width
    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle's width.

        Args:
            value (int): The new size of the Rectangle's width.

        Raises:
            TypeError: If the provided width is not an integer.
            ValueError: If the provided width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
    
    @property
    def height(self):
        """int: height of the rectangle"""
        return self.height
    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle's height.

        Args:
            value (int): The new size of the Rectangle's height.

        Raises:
            TypeError: If the provided height is not an integer.
            ValueError: If the provided height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
