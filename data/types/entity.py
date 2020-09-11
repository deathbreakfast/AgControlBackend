import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.entity import Entity as EntityModel


class Entity(SQLAlchemyObjectType):
    class Meta:
        model = EntityModel
        interfaces = (graphene.relay.Node,)


class EntityAttribute:
    serial = graphene.String()


class CreateEntityInput(graphene.InputObjectType, EntityAttribute):
	pass
