#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 2022
@author: Godday Okoduwa
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
