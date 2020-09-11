from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from ..database.base import Base


class Entity(Base):
	__tablename__ = 'entity'

	id = Column(Integer, primary_key=True)
	serial = Column(String)	
