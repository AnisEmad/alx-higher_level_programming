#!/usr/bin/python3
""" this module for Square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ this Square class inherit from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string repersentation of class square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ getter of size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method that updates the attributes of the class """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ turns the class to a dictiontry """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
