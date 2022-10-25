#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from json file

    Arguments:
        filename (str): The name of the output file

    Return:
        A json string read from file.
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
