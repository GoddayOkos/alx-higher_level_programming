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
    def __init__(self, size):
        """The __init__ method for Square class

        Args:
            size: A private attribute
        """
        self.__size = size
