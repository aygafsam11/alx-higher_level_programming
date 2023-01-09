dator functions
Raises:
    Exception: area is not#!/usr/bin/python3
"""
This module implements a base class for Geometry objects,
with attribute vali implemented
    TypeError: [attribute] must be an integer
    ValueError: [attribute] ,must be greater than 0
"""


class BaseGeometry:
    """base class
    """
    def area(self):
        """find area
        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check value
 tion
            value (any): value to check
            Args:
            name (str): value designa   Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
