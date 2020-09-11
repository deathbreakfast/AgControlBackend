import graphene

from ..database.db_session import db_session
from ..models.entity import Entity as EntityModel
from ..types.entity import Entity, CreateEntityInput
from ..utils.input_to_dictionary import input_to_dictionary


class CreateEntity(graphene.Mutation):
    entity = graphene.Field(lambda: Entity)
    ok = graphene.Boolean()

    class Arguments:
        input = CreateEntityInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        entity = EntityModel(**data)
        db_session.add(entity)
        db_session.commit()
        ok = True
        return CreateEntity(entity=entity, ok=ok)


class Mutation(graphene.ObjectType):
	createEntity = CreateEntity.Field()
