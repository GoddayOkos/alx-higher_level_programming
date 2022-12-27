#!/usr/bin/python3
"""
Created on Tue Dec 27 2022

@author: Godday Okoduwa"
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    db_name = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usermane, password, db_name))
    # create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
