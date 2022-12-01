import os
from datetime import datetime

from sqlalchemy import Integer, String, Column, Date, ForeignKey, Float, DATE

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, scoped_session

DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:qwerty1234567@localhost:3306/pp")

engine = create_engine(DB_URL)

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__="user"

    idUser = Column(Integer, primary_key=True)
    Email = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)
    FirstName = Column(String(25), nullable=False)
    LastName = Column(String(225), nullable=False)
    Role = Column(String(225), nullable=False)

class Booking(Base):
    __tablename__="booking"

    Booking = Column(Integer, primary_key=True)
    User = Column(Integer)
    Car = Column(Integer)
    bfrom = Column(DATE, nullable=False)
    buntil = Column(DATE, nullable=False)

class Car(Base):
    __tablename__="car"

    idCar = Column(Integer, primary_key=True)
    brand = Column(String(225))
    model = Column(String(225))
    year = Column(Integer)
    seatsNum = Column(Integer)
    status =  Column(String(225))
    Price = Column(Float)