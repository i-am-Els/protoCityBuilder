import json, os
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

        # Check if the entity references a prefab
        if "prefab" in entity_dict:
            prefab_name = entity_dict["prefab"]
            prefab_path = os.path.join("assets", "prefabs", "prefab.json")
            
            if not os.path.exists(prefab_path):
                raise ValueError(f"Prefab file not found at {prefab_path}")
            
            # Load the prefab definition
            with open(prefab_path, "r") as prefab_file:
                prefab_generator = (item for item in json.load(prefab_file).get("spawnables", []) if item["name"] == prefab_name)
                try:
                    prefab_dict = next(prefab_generator)  # Get the first matching dictionary from the generator
                except StopIteration:
                    raise ValueError(f"Prefab '{prefab_name}' not found in {prefab_path}")

            # Merge the prefab with the entity's overrides
            merged_dict = cls._merge_dicts(prefab_dict, entity_dict.get("overrides", {}))
            entity_dict = merged_dict

            # prevent possible overrides of non component values
            entity_dict["name"] = entity.name
            entity_dict["description"] = entity.description
            entity_dict["tags"] = entity.tags

        for component_dict in entity_dict["components"]:
            type_name = component_dict["type"]
            component_class = ComponentsRegistry.component_registy().get(type_name, ComponentsBase)
            if component_class:
                component = component_class.make_from_dict(entity_dict["name"], component_dict)
                entity.add_component(component)
            else:
                raise ValueError(f"Unknown component type: {type_name}")
        return entity


    @staticmethod
    def _merge_dicts(base_dict, override_dict):
        """
        Merge two dictionaries. The override_dict values take precedence.

        It is expected that the components list is the only key-value pair in override_dict and it might contain values that don't already exist in the component's array of base_dict.
        
        Return: An updated version of base_dict that has been merged with values both new and overriden values from override_dicts.

        """

        merged = base_dict.copy()

        for key, override_value in override_dict.items():
            if key != "components":
                # For normal keys, the override takes precedence
                merged[key] = override_value
            else:
                # For the 'components' key, we need to merge list elements by matching 'type'
                base_components = merged.get("components", [])
                # Create a lookup dictionary for quick access by component type
                base_by_type = {comp.get("type"): comp for comp in base_components}
                
                for override_comp in override_value: # override_value is expected to be a list of components
                    comp_type = override_comp.get("type")
                    if comp_type in base_by_type:
                        # Merge the override into the corresponding base component
                        base_by_type[comp_type].update(override_comp)
                    else:
                        # If the type isn't present, add the new component to the list
                        base_components.append(override_comp)
                
                # Update the merged dict with the updated list of components
                merged["components"] = base_components
        
        return merged



