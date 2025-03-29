from typing import Dict
from scripts.core.entity import Entity


class Scene:
    def __init__(self, name):
        self.name = name
        self.entities: Dict[str, Entity] = {}
        print(f"Scene {self.name} loaded")

    def add_entity(self, entity):
        self.entities[entity.name] = entity

    def render(self):
        # print(f"Rendering scene {self.name}")
        for entity in self.entities.values():
            entity.render()

    def remove_entity(self, entity):
        if self.entities.get(entity.name):
            del self.entities[entity.name]
            self.entities.remove(entity)

    def get_entity(self, name):
        return self.entities.get(name, None)
    
    def get_entities(self):
        return self.entities
    
    def has_entity(self, name):
        return self.entities.get(name, None) is not None

    @classmethod
    def make_from_dict(cls, scene_dict: dict):
        scene = cls(scene_dict["scene_name"])
        for entity_dict in scene_dict["entities"]:
            entity = Entity.make_from_dict(entity_dict)
            scene.add_entity(entity)
        return scene
