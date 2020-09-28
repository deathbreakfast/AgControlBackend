import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean
from sqlalchemy.orm import backref, relationship 

from ..database.base import Base
from .sprinkler import Sprinkler

class EntityType(enum.Enum):
    sprinkler = 'sprinkler'
    unknown = 'unknown'
    zone = 'zone'

class Entity(Base):
    __tablename__ = 'entity'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(EntityType), default=EntityType.unknown)
    name = Column(String)
    show_on_dashboard = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey('entity.id'))
    
    children = relationship('Entity',
                backref=backref('parent', remote_side=[id])
                )
    sprinkler = relationship('Sprinkler', back_populates='entity')
