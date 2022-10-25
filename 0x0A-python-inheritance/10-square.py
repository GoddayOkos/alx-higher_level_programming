#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 2022

@author: Godday Okoduwa
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class shape, inheirts from Rectangle
    """
    def __init__(self, size):
        """
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Return:
            The area of the square
        """
        return self.__size ** 2
