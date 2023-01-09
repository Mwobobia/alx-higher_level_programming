#!/usr/bin/python3
""" This is a function """


class MyList(list):
    """ print new list """

    def print_sorted(self):
        """Method that sorted a list"""

        print(sorted(list(self)))
