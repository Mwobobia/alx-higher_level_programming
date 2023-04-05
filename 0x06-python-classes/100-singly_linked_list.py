#!/usr/bin/python3
"""
Create a Singly linked list.
"""


class Node:
    """
    individual node
    """
    def __init__(self, data, next_node=None):
        if type(data) != int:
            print("data must be an integer", end="")
            raise TypeError
        else:
            self.__data = data
        if next_node is not None:
            if isinstance(next_node, Node) is not True:
                print("next_node must be a Node object", end="")
                raise TypeError
            else:
                self.__next_node = next_node
        else:
            self.__next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if type(value) != int:
                print("data must be an integer", end="")
                raise TypeError
            else:
                self.__data = value

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if next_node is not None:
                if isinstance(value, Node) is not True:
                    print("next_node must be a Node object", end="")
                    raise TypeError
                else:
                    self.__next_node = value
            else:
                self.__next_node = value

"""
SinglyLinkedList.
"""


class SinglyLinkedList:
    """
    singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        yes = 0
        node = Node(value, None)
        if self.__head is None:
            self.__head = node
        else:
            another_node = self.__head
            prev_n = another_node
            next_n = self.__head._Node__next_node
            if another_node._Node__data >= value and next_n is None:
                node._Node__next_node = self.__head
                self.__head = node
            elif another_node._Node__data <= value and next_n is None:
                self.__head._Node__next_node = node
            else:
                if self.__head._Node__data > value:
                    self.insert_head(self.value)
                    return

                while another_node is not None:
                    if int(another_node._Node__data) < int(value):
                        prev_n = another_node
                        another_node = next_n
                        if another_node is not None:
                            next_n = another_node._Node__next_node
                        else:
                            next_n = None
                    else:
                        prev_n._Node__next_node = node
                        node._Node__next_node = another_node
                        yes = 1
                        break
                if yes == 0:
                    prev_n._Node__next_node = node

        def insert_head(self, value):
            node = Node(value, None)
            another_node = self.__head
            self.__head = node
            self.__head._Node__next_node = another_node

        def __str__(self):
            s = ""
            node = self.__head
            while node is not None:
                if node._Node__next_node is not None:
                    s += str(node._Node__data) + "\n"
                else:
                    s += str(node._Node__data)
                node = node._Node__next_node
            return s
