from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URI

Base = declarative_base()
engine = create_engine(DATABASE_URI)

class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    brand = Column(String(250))
    model = Column(String(250))
    status = Column(String(250))

    def __repr__(self):
        return "<Car(brand='{}', model='{}', status='{}')>" \
            .format(self.brand, self.model, self.status)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    name = Column(String(250))
    surname = Column(String(250))
    username = Column(String(250))
    password = Column(String(250))
    role = Column(Integer())

    def __repr__(self):
        return "<User(name='{}')>" \
            .format(self.name)


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer())
    car_id = Column(Integer())
    beginningDate = Column(DateTime)
    amountOfDays = Column(Integer)
    complete = Column(String(250))

    def __repr__(self):
        return "<Order(user='{}', car='{}', beginningDate='{}', amountOfDays={}, complete='{}')>" \
            .format(self.user_id, self.car_id, self.beginningDate, self.amountOfDays, self.complete)

