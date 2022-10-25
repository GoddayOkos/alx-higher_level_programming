#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 2022

@author: Godday Okoduwa
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# try:
new_list = load_from_json_file('add_item.json')
# except Exception:
#   new_list = []

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

# try:
save_t_json_file(new_list, 'add_item.json')
# except Exception:
#    pass
