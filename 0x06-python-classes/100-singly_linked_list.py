#!/usr/bin/python3
"""
Create a class Node that defines a node of a singly linked list by:
- data and next_node private properties
- getters and setters
"""


class Node:
    """Class Node"""
    def __init__(self, data, next_node=None):
        """Constructor for Node"""
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Getter of the private attribute data"""
        return (self._data)
    
    @data.setter
    def data(self, value):
        """Setter for the private attribute data"""
        if (type(value) is not int):
            raise(TypeError("data must be an integer"))
        else:
            self._data = value

    @property
    def next_node(self):
        """Getter for the next node"""
        return (self._next_node)
    
    @next_node.setter
    def next_node(self, value):
        """Setter for the next node"""
        if (value is None or isinstance(value, Node)):
            self._next_node = value
        else:
            raise(TypeError("next_node must be a Node object or None"))

class SinglyLinkedList:
    """ class SinglyLinkedList that defines a singly linked list """
    def __init__(self):
        """Constructor function"""
        self._head = None

    def sorted_insert(self, value):
        """ return a sorted list of values"""
        new_node = Node(value)

        if (self._head is None or value < self._head.data):
            new_node.next_node = self._head
            self._head = new_node
            return
        
        current = self._head
        while (current.next_node is not None and current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        result = []
        current = self._head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
    
