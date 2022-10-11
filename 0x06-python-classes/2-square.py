#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 2022
@author: Godday Okoduwa
"""


class Square:
    """Class Square with a private attribute

    Attributes:
        size: Size of the square
    """
    def __init__(self, size=0):
        """The __init__ method for Square class

        Args:
            size: A private attribute

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
