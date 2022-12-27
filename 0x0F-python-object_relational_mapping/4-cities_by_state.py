#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 2022

@author: Godday Okoduwa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    db_name = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities INNER JOIN states\
                   ON cities.states_id=states.id\
                   ORDER BY cities.id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
