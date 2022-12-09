from sqlalchemy import Column, Integer, String
from database import base

class user_table(base):
    __tablename__= "user_table"


    id = Column(Integer)
    email = Column(String)
    password = Column(String)

lass item_table():
    __tablename__= "item_table"


    id = Column(Integer)
    name = Column(String)
    user = Column(String)    