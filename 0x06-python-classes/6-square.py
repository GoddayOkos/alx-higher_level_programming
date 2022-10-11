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
    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method for Square class

        Args:
            size: A private attribute
            position: A public attribute rep. x and y coord.
        """
        self.position = position
        self.size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            Area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Call the function to checking property

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """validate value and update size attribute

        Args:
            value: Value to update size with

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print a square using # character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(end=" ")
                for k in range(self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Getter for property

        Returns:
            The tuple position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Validate value and update position

        Args:
            value: value to update position with

        Raises:
            TypeError: Exception if value is not an integer
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
