#!/usr/bin/python3
""" defining a rectangle class """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """


    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """ width of the rectangle """
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """ the height of the rectangle """
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x of the rectangel """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y of the rectangle """
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculates the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ display the rectangle """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                    print(" ",end="")
            for j in range(self.__width):
                print("#",end="")
            print()

    def __str__(self):
        """ returns the representation of the rectangle"""
        str = "[Rectangle] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__width)
        str += "/{}".format(self.__height)
        return str

    def update(self, *args, **kwargs):
        """ update the recatngle"""
        n = len(args)
        if n == 0:
            for key, item in kwargs.items():
                if key == "id":
                    self.id = item
                elif key == "width":
                    self.__width = item
                elif key == "height":
                    self.__height = item
                elif key == "x":
                    self.__x = item
                elif key == "y":
                    self.__y = item
        else:
            if n > 0:
                self.id = args[0]
            if n > 1:
                self.__width = args[1]
            if n > 2:
                self.__height = args[2]
            if n > 3:
                self.__x = args[3]
            if n > 4:
                self.__y = args[4]
