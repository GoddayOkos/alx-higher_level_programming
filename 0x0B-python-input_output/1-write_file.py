#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""


def write_file(filename="", text=""):
    """
    Writes the given text into the given file.

    Arguements:
        filename (str): The name of the file to write to
        text (str): The text to write into the file

    Returns:
        The number of characters written into the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
