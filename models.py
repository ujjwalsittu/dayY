from database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = 'registeredUsers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(150))
    email = Column(String(255))
