#!/usr/bin/python3
"""
This module defines a simple Square class.

This module provides a basic implementation of a Square class that can be used
to represent squares in a geometric context. The class has been updated to
include an attribute for size, along with error handling for invalid sizes.

Example:
    # Create an instance of the Square class with a specified size
    my_square = Square(5)
"""


class Square:
    """
    A class to represent squares.

    This class defines a square with a size attribute and provides error
    handling
    for invalid size values.

    Attributes:
        __size (int): The size of the square's sides.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is negative.
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance with a specified size.

        Args:
            size (int): The size of the square's sides.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
