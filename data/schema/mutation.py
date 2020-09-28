import graphene

from ..database.db_session import db_session
from ..models.entity import Entity as EntityModel, EntityType
from ..models.sprinkler import Sprinkler as SprinklerModel
from ..types.entity import Entity, CreateEntityInput, EditEntityInput
from ..types.sprinkler import Sprinkler, EditSprinklerInput
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
        return CreateEntity(entity=entity, ok=True)


class EditEntity(graphene.Mutation):
    entity = graphene.Field(lambda: Entity)
    ok = graphene.Boolean()

    class Arguments:
        input = EditEntityInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        entity = EntityModel.query.get(data['id'])

        if 'entity_type' in data:
            if entity.type == EntityType.sprinkler and data['entity_type'] != 'sprinkler':
                db_session.delete(SprinklerModel.query.get(entity.sprinkler[0].id))
            elif entity.type == EntityType.zone or EntityType.unknown and \
                    data['entity_type'] == 'sprinkler':
                        sprinkler = SprinklerModel(entity_id=entity.id)
                        db_session.add(sprinkler)

            entity.type = data['entity_type'] 
                

        if 'name' in data:
            entity.name = data['name']

        if 'show_on_dashboard' in data:
            entity.show_on_dashboard = data['show_on_dashboard']

        if 'parent_id' in data:
            entity.parent_id = data['parent_id']

        db_session.add(entity)
        db_session.commit()
        return EditEntity(ok=True, entity=entity)


class EditSprinkler(graphene.Mutation):
    sprinkler = graphene.Field(lambda: Sprinkler)
    ok = graphene.Boolean()

    class Arguments:
        input = EditSprinklerInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        sprinkler = SprinklerModel.query.get(data['id'])

        if 'serial' in data:
            sprinkler.serial = data['serial']

        if 'ip_address' in data:
            sprinkler.ip_address = data['ip_address']

        db_session.add(sprinkler)
        db_session.commit()

        return EditSprinkler(ok=True, sprinkler=sprinkler)



class Mutation(graphene.ObjectType):
    createEntity = CreateEntity.Field()
    editEntity = EditEntity.Field()
    editSprinkler = EditSprinkler.Field()


