from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from apps.db import engine, Base
from sqlalchemy.orm import sessionmaker, Session

import apps.db as db
import apps.items.models as models

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app=FastAPI()
class user(BaseModel):
    id : int
    email : str = Field(min_length=1)
    password : str = Field(min_length=1)

    class validation:
        schema={
            "example":{
                "id" : "123",
                "email" : "amanyu.r@accubits.com",
                "password" : "accubits123" 
            }
        }


@app.get('/')
async def hellow():
    return "hello world"

@app.post('/signup')
async def create_user(email:str, password:str):
    db_user = models.User(email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
  
@app.get('/login')
async def login(email_login: str,password_login: str):
    return db.query(models.User).filter(models.User.email == email_login and models.User.password == password_login).first()

@app.get('/item')           
async def viewitems(user_id : int):
    return db.query(models.Item).filter(models.Item.userid == user_id)

@app.post('/items')
async def additem(itemid : int, itemname : str):
    db_item = models.Item(id=itemid, name=itemname)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get('/item1')
async def viewitem(itemid : int):
    return db.query(models.Item).filter(models.Item.id == itemid)

#@app.put('/item2')
#async def updateitem(itemid : int):

@app.delete('/items3')
async def deleteitem(itemid : int):
    db.query(models.Item).filter(models.Item.id == itemid)
    