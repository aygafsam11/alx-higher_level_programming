#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for i TypeError('size must be an integer')
        elifts attributes
"""


class Square:
    """Square implementation
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
