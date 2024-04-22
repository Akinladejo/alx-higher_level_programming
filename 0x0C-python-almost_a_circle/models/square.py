#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Calss"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initalizates a Square class instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update a Square"""
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if kwargs:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
            """returns the dictionary representation of a Square"""
            dictionary = {
                            "id": self.id,
                            "size": self.size,
                            "x": self.x,
                            "y": self.y
                         }
            return dictionary
