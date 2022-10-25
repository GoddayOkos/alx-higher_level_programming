#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author; Godday Okoduwa
"""
import json


def to_json_string(my_obj):
    """
    Returs a json string containing object's representation

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json string representation of the object
    """
    return json.dumps(my_obj)
