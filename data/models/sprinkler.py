import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import backref, relationship

from ..database.base import Base


class SprinklerStatus(enum.Enum):
    inactive = 'inactive'
    running = 'running'
    off = 'off'


class Sprinkler(Base):
    __tablename__ = 'sprinkler'

    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey('entity.id'))
    status = Column(Enum(SprinklerStatus), default=SprinklerStatus.off)
    serial = Column(String)
    ip_address = Column(String)

    entity = relationship('Entity', back_populates='sprinkler', foreign_keys=entity_id, uselist=False)
