#!/usr/bin/python3
def add_attribute(clas, att, val):
    try:
        new = clas()
        new.att = val
    except:
        raise TypeError("can't add new attribute")
