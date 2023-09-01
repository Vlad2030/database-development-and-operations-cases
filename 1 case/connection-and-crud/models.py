import datetime

from database import Base
from sqlalchemy import DATETIME, Column, Integer, String


class PetsDatabase(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer, default=0.0)
    type = Column(String)
    breed = Column(String)
    datetime = Column(DATETIME, default=datetime.datetime.now())