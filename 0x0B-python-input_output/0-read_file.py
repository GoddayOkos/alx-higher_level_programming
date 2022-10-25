#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""


def read_file(filename=""):
    """
    Reads the file

    Argument:
        filename (str): The name of the file to read
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
