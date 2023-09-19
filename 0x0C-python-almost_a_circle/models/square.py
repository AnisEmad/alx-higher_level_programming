#!/usr/bin/python3
""" defining a square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size of the square """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ returns string representation of the square """
        str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return str

    def update(self, *args, **kwargs):
        """ upadte the sqaure """
        if args:
            n = len(args)
            if n > 0:
                self.id = args[0]
            if n > 1:
                self.size = args[1]
            if n > 2:
                self.x = args[2]
            if n > 3:
                self.y = args[3]
        elif kwargs:
            for key, item in kwargs.items():
                if key == "id":
                    self.id = item
                elif key == "size":
                    self.size = item
                elif key == "x":
                    self.x = item
                elif key == "y":
                    self.y = item
