import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.sprinkler import Sprinkler as SprinklerModel


class Sprinkler(SQLAlchemyObjectType):
    class Meta:
        model = SprinklerModel
        interfaces = (graphene.relay.Node,)


class EditSprinklerAtribute:
    id = graphene.String(required=True)
    serial = graphene.String()
    ip_address = graphene.String()


class EditSprinklerInput(graphene.InputObjectType, EditSprinklerAtribute):
    pass
