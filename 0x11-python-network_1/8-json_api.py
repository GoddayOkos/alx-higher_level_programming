#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 2023

@author: Godday Okoduwa
"""
from requests import post, codes
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = {'q': ''}
    response = post(url, data=q)
    try:
        obj = response.json()
        if len(obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(obj['id'], obj['name']))
    except Exception:
        print('Not a valid JSON')
