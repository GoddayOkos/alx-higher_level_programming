#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""


def class_to_json(obj):
    """
    Creates a json representation of an object

    Arguments:
        obj (obj): The object inputted to create a class

    Return:
        A json representation of obj
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
