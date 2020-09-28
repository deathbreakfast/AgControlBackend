import graphene

from ..schema.query import Query
from ..schema.mutation import Mutation

from ..types.entity import Entity
from ..types.sprinkler import Sprinkler

types = [
	Entity,
        Sprinkler,
]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)

