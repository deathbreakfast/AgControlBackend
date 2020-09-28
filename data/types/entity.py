import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.entity import Entity as EntityModel, EntityType


class Entity(SQLAlchemyObjectType):
    class Meta:
        model = EntityModel
        interfaces = (graphene.relay.Node,)


class CreateEntityAttribute:
    entity_type = graphene.String(required=False)
    name = graphene.String(required=False)
    parent_id = graphene.String(required=False)
    show_on_dashboard = graphene.Boolean(required=False)


class EditEntityAttribute:
    id = graphene.String(required=True)
    entity_type = graphene.String(required=False)
    name = graphene.String(required=False)
    parent_id = graphene.String(required=False)
    show_on_dashboard = graphene.Boolean(required=False)



class CreateEntityInput(graphene.InputObjectType, CreateEntityAttribute):
    pass


class EditEntityInput(graphene.InputObjectType, EditEntityAttribute):
    pass

