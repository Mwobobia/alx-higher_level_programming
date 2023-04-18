#!/usr/bin/python3
""" Square class inherits form rectangle"""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """square"""

    def __str__(self):
        """ returns square discryption"""
        st = "[Square] (" + str(self.id) + ') '
        st += str(self._Rectangle__x) + '/' + str(self._Rectangle__y)
        st += ' - ' + str(self._Rectangle__width)
        return st

    @property
    def size(self):
        """ size getter"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """ size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates square"""
        if (args) and args != ():
            if len(args) >= 1:
                super(Rectangle, self).__init__(args[0])
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    super(Rectangle, self).__init__(v)
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """ makes dictionary out of square data"""
        dic = {'id': self.id, 'x': self._Rectangle__x,
               'y': self._Rectangle__y, 'size': self._Rectangle__width}
        return dic

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super(Square, self).__init__(size, size, x, y, id)
