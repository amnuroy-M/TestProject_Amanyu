from fastapi import FastAPI
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,index=True)
    password = Column(String)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    userid = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")


