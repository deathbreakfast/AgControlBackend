from .db_session import db_session, engine
from .base import Base


def init_db(**kwargs):

    if kwargs['dump_tables']:
        Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine)

    if kwargs['test_data']:
        from ..models.entity import Entity, EntityType
        from ..models.sprinkler import Sprinkler
        test_zone = Entity(name='Test Zone', type=EntityType.zone)
        test_entity = Entity(name='The test sprinkler', 
                type=EntityType.sprinkler, parent=test_zone)
        test_sprinkler = Sprinkler(entity=test_entity, serial='TEST_SERIAL', ip_address='127.0.0.1')
        db_session.add(test_zone)
        db_session.add(test_entity)
        db_session.add(test_sprinkler)
        db_session.commit()

