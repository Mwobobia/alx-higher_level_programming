#!/usr/bin/python3
""" base class for all shapes"""


import json
import turtle
import os


class Base():
    """ BaseClass of all shapes"""

    __nb_objects = 0

    def draw(list_rectangles, list_squares):
        """ draws shape with turtle"""
        for i in list_rectangles:
            tur = turtle.Turtle()
            tur.color("red")
            tur.pensize(6)
            tur.shape('turtle')
            tur.forward(i.__width)
            tur.left(90)
            tur.forward(i.__height)
            tur.left(90)
            tur.forward(i.__width)
            tur.left(90)
            tur.forward(i.__height)
        for i in list_squares:
            tur = turtle.Turtle()
            tur.color("blue")
            tur.pensize(6)
            tur.shape('turtle')
            tur.forward(i.__width)
            tur.left(90)
            tur.forward(i.__height)
            tur.left(90)
            tur.forward(i.__width)
            tur.left(90)
            tur.forward(i.__height)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves data for shape to csv"""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w+') as f:
            f.seek(0)
            lst = []
            for i in list_objs:
                st = ''
                st += str(i.id) + ', '
                if cls.__name__ == "Rectangle":
                    st += str(i.__width) + ', ' + str(i.__height) + ', '
                else:
                    st += str(i.__width) + ', '
                st += str(i.__x) + ', ' + str(i.__y)
                lst += st
            f.write(lst)

    @classmethod
    def load_from_file_csv(cls):
        """ loads data from csv """
        filename = cls.__name__ + '.csv'
        with open(filename, 'r+') as f:
            lst = json.load(f.read())
            ret = []
            new = cls(1, 1)
            for i in lst:
                ret += [new.update(i)]
            return ret

    @classmethod
    def load_from_file(cls):
        """ loads from json file"""
        filename = str(cls.__name__) + ".json"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r+', encoding='utf-8') as f:
            ret = []
            dics = Base.from_json_string(f.read())
            for i in range(len(dics)):
                new = cls.create()
                new.update(**dics[i])
                ret += [new]
            return ret

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves to json file"""
        filename = str(cls.__name__) + '.json'
        with open(filename, 'w+', encoding='utf-8') as f:
            f.seek(0)
            obj_list = []
            if list_objs is None or len(list_objs) == 0:
                f.write(Base.to_json_string(obj_list))
            else:
                for obj in list_objs:
                    obj_list += [obj.to_dictionary()]
                f.write(Base.to_json_string(obj_list))

    @classmethod
    def create(cls, **dictionary):
        """ creates shape from dictionary"""
        if cls.__name__ == 'Square':
            new = cls(1)
        else:
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @staticmethod
    def from_json_string(json_string):
        """ changes from json string to real"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ changes to json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
