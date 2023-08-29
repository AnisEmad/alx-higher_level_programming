#!/usr/bin/python3
"""
This module defines a simple Square class.

This module provides a basic implementation of a Square class that can be used
to represent squares in a geometric context. The class has been updated to
include
an attribute for size.

Example:
    # Create an instance of the Square class with a specified size
    my_square = Square(5)
"""


class Square:
    """
    A class to represent squares.

    This class defines a square with a size attribute.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size):
        """
        Initialize a Square instance with a specified size.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
