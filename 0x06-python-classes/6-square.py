#!/usr/bin/python3
"""
This module defines a simple Square class.

This module provides a basic implementation of a Square class that can be used
to represent squares in a geometric context. The class includes an attribute
for size, along with error handling for invalid sizes.

Example:
    # Create an instance of the Square class with a specified size
    my_square = Square(5)
"""


class Square:
    """
    A class to represent squares.

    This class defines a square with a size attribute and provides error
    handling for invalid size values.

    Attributes:
        size (int): The size of the square's sides.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is negative.

    Methods:
        area(): Calculates the area of the square.
        my_print(): prints the square with character #.
        my_print(): prints the square with character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with a specified size.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
        self.__poistion = position
    @property
    def position(self):
        return self.__poistion
    
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__poistion = value 
    @property
    def size(self):
        """int: The size of the square's sides."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square's sides.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The calculated area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for lines in range(self.__poistion[1]):
                    print()
                for lol in range(self.__poistion[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
