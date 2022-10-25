#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save object to a file as json string

    Arguments:
        my_obj (obj): The inputed object to convert in json format
        filename (str): The name of the output file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
