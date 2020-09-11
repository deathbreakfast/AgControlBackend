import graphene

from ..schema.query import Query
from ..schema.mutation import Mutation

from ..types.entity import Entity

types = [
	Entity,
]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)

