from typing import Type
from scripts.core.components_base import ComponentsBase

class System:
    _component_type = None
    _is_enabled = True
    def __init__(self, component_type):
        self._component_type: Type[ComponentsBase] = component_type
        self.components = []
    
    @property
    def id(self):
        return id(self)

    def add_component(self, component):
        if component not in self.components:
            self.components.append(component)

    def remove_component(self, component):
        if component in self.components:
            self.components.remove(component)

    def update(self):
        if not self._is_enabled:
            return
        for component in self.components:
            component.update()

    def start(self):
        if not self._is_enabled:
            return
        for component in self.components:
            component.start()

    def awake(self):
        if not self._is_enabled:
            return
        for component in self.components:
            component.awake()

    def on_destroy(self):
        for component in self.components:
            component.on_destroy()

    def create_component(self, entity, *args, **kwargs):
        component = self.make_component(entity, self, *args, **kwargs)
        return component

    @classmethod
    def make_component(cls, entity, system, *args, **kwargs):
        return cls._component_type(entity, system, *args, **kwargs)

    @classmethod
    def disable_system(cls):
        cls._is_enabled = False

    @classmethod
    def enable_system(cls):
        cls._is_enabled = True
