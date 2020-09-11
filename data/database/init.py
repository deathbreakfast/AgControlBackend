from .db_session import db_session, engine
from .base import Base


def init_db():
    from ..models.entity import Entity 

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    test_entity = Entity(serial='TEST_SERIAL')
    db_session.add(test_entity)
    db_session.commit()
