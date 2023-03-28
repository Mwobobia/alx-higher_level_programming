#!/usr/bin/python3
# 0-square.py
"""A module that defines a square """


class Square:
    """A class that represents a Square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represents size of the square defined
        Raises:
            TyreError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
