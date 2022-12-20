#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes
"""


class Square:
    """Square implementation
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    dmust be an integer')
        elif size < 0:
      ef size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size       raise ValueError('size must be >= 0')
      g size
        """
        if (self.__size == 0):
  self.__size = size

    def area(self):
        """calculates the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints a square  with the correspondin            print('')

        for l in range(self.__size):
            print('#' * self.__size)
