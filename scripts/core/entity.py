from typing import List
from scripts.core.components_base import ComponentsBase
from scripts.core.component_registry import ComponentsRegistry

class Entity:
    def __init__(self, name: str, description: str=None):
        self.name = name
        self.description = description
        self.components: List[ComponentsBase] = []
        self.tags: List[str] = []
        print(f"Entity {self.name} started")

    def __str__(self):
        return f"{self.name} is {self.description} and is located at {self.location}"
    
    def add_component(self, component: ComponentsBase):
        self.components.append(component)
        component.entity = self  # Assuming each component has a reference to its entity
        component.awake()  # Call the awake method when the component is added
        component.start()
        component.on_enable()

    def remove_component(self, component: ComponentsBase):
        if component in self.components:
            self.components.remove(component)
            component.on_disable()  # Call the on_disable method when the component is removed
            component.on_destroy()  # Call the on_destroy method when the component is removed
            component.entity = None  # Remove the reference to the entity

    def get_component(self, component_type: type) -> ComponentsBase:
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None
    
    def get_components(self, component_type: type) -> List[ComponentsBase]:
        return [component for component in self.components if isinstance(component, component_type)]
    
    def has_component(self, component_type: type) -> bool:
        return any(isinstance(component, component_type) for component in self.components)
    
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags
    
    def make_entity(self, name: str, description: str=None):
        return Entity(name, description)
    
    @classmethod
    def make_from_dict(cls, entity_dict: dict):
        entity = Entity(entity_dict["name"])
        entity.description = entity_dict.get("description", None)
        entity.tags = entity_dict.get("tags", [])
        for component_dict in entity_dict["components"]:
            type_name = component_dict["type"]
            component_class = ComponentsRegistry.component_registy().get(type_name, ComponentsBase)
            if component_class:
                component = component_class.make_from_dict(entity_dict["name"], component_dict)
                entity.add_component(component)
            else:
                raise ValueError(f"Unknown component type: {type_name}")
        return entity
