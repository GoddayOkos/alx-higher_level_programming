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
    if len(args) != 5:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    db_name = args[3]
    state_name = args[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    # create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    states = session.query(State).filter(State.name == state_name)\
                    .order_by(State.id)
    if states is not None and states.count() > 0:
        for state in states:
            print('{}'.format(state.id))
    else:
        print('Not found')
