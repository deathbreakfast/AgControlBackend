import graphene
from graphene import relay

from ..models.entity import Entity as EntityModel
from ..types.entity import Entity


class Query(graphene.ObjectType):
	node = relay.Node.Field()

	all_entities = graphene.List(Entity)

	@staticmethod
	def resolve_all_entities(parent, info, **args):
		query = Entity.get_query(info)
		return query.all()
