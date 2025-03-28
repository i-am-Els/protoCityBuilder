from typing import Dict, Type
from scripts.core.accessor import Accessor
from scripts.core.components_base import ComponentsBase
from scripts.core.scene import Scene
from scripts.core.systems import System


class Game:
    def __init__(self):
        self.scenes: Dict[str, Scene] = {}
        self.current_scene: Scene = None
        self.systems: Dict[Type[ComponentsBase], System] = {}
        Accessor.add_accessor(name="Game", obj=self)

    def _set_quit_callback(self, callback):
        self.callback = callback

    def _add_system(self, system: System):
        for sys in self.systems.values():
            if sys._component_type == system._component_type or sys.id == system.id:
                return
        self.systems[system._component_type] = system

    def get_systems(self) -> Dict[Type[ComponentsBase], System]:
        return self.systems
    
    def get_system(self, component_type: Type[ComponentsBase]) -> System:
        return self.systems.get(component_type, None)

    def add_scene(self, scene: Scene, make_current=False):
        if make_current:
            self.current_scene = scene
        if self.scenes.get(scene.name):
            return
        self.scenes[scene.name] = scene

    def set_current_scene(self, scene_name):
        scene = self.get_scene(scene_name)
        self.current_scene = scene

    def get_current_scene(self):
        return self.current_scene
    
    def get_scene(self, name):
        return self.scenes.get(name, None)
    
    def get_scenes(self):
        return self.scenes

    def has_scene(self, name):
        return self.scenes.get(name, None) is not None
    
    def quit(self):
        self.current_scene = None
        self.scenes = {}
        self.systems = []
        print("Game quit")
        if self.callback:
            self.callback()
    
    def remove_scene(self, scene):
        if self.has_scene(scene.name):
            self.scenes.remove(scene)