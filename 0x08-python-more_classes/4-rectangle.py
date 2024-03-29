#!/usr/bin/python3

"""
empty class Rectangle
"""


class Rectangle:
    """
    Rectangle empty class
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for item in range(self.__height):
            if item != self.__height - 1:
                string = string + "#" * self.__width + "\n"
            else:
                string = string + "#" * self.__width
        return string

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + \
                str(self.__height) + ")"
