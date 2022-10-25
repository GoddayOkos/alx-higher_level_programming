#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""


class BaseGeometry():
    """
    An empty class
    """
    
    def area(self):
        """
        Public instance method that calculates the area

        Rasises:
            Exception if area is not imlemented
        """
        raise Exception("area() is not implemented")
