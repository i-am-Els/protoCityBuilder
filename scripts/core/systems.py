from typing import Type
from scripts.core.components_base import ComponentsBase

class System:
    # _component_type = None
    _is_enabled = True
    def __init__(self, component_type, is_static: bool=False):
        self._component_type: Type[ComponentsBase] = component_type
        self.__components = []
        self.__static = is_static
        print(f"{self._component_type.__name__} System started")

    @property
    def id(self):
        return id(self)

    @property
    def static(self):
        return self.__static
    
    @property
    def components(self):
        return self.__components
    
    @components.setter
    def components(self, value):
        return

    def add_component(self, component):
        if component not in self.components:
            self.components.append(component)

    def remove_component(self, component):
        if component in self.components:
            self.components.remove(component)

    def update(self):
        if self.static or not self._is_enabled:
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
        component = self._component_type(entity, *args, **kwargs)
        return component

    @staticmethod
    def make_component(component_type: Type[ComponentsBase], entity, *args, **kwargs):
        return component_type(entity, *args, **kwargs)

    @classmethod
    def disable_system(cls):
        cls._is_enabled = False

    @classmethod
    def enable_system(cls):
        cls._is_enabled = True
