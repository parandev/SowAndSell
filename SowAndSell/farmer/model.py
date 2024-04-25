import db
from db.base import Base
from sqlalchemy import Column, String, Integer


class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), index=True, nullable=False)
    total_land_in_acres = Column(Integer)
    address = Column(String(256), nullable=True)
