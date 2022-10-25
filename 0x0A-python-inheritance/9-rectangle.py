#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inheirts from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str funtion for rectangle

        Returns:
            string representation of Rectangle
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """
        Calculates the area of the rectangle

        Return:
            The area of the rectangle
        """
        return self.__width * self.__height
