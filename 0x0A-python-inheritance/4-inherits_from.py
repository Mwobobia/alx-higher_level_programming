#!/usr/bin/python3
"""this is a function """


def inherits_from(obj, a_class):
    """ return true or flase"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
