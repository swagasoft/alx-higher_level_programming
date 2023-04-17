#!/usr/bin/python3
"""Define Square class implement Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class body
"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization class props in constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ return width size
        """
        return self.width

    @size.setter
    def size(self, value):
        """module Square height and width
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Square class string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """update square props
        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return dict of class props
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
