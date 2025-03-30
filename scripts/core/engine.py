import json, os
from typing import Dict, Type
from scripts.core.accessor import Accessor
from scripts.core.components_base import ComponentsBase
from scripts.core.game import Game
from scripts.core.scene import Scene
from scripts.core.systems import System

def clear_screen(next_message):
    """
    Clears the console screen.
    Works for both Windows and Unix-based systems.
    """
    # Check the operating system and execute the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')
    print(next_message)


class Engine:
    def __init__(self, name):
        self.name = name
        self.game = Game()
        self.add_scene(scene=Scene(name="Main"))
        self.set_current_scene(scene=self.game.get_scene(name="Main"))
        self.is_running = True
        self.game._set_quit_callback(self.quit)
        self.ui = None
        Accessor.add_accessor("Engine", self)
        print("Engine started")

    def add_systems_from_classes(self, component_classes: Dict[Type[ComponentsBase], bool]):
        """
        This function takes in a map of Component types and the is_static state the system controlling that class should have.
        """
        for component_class , is_static in component_classes.items():
            system = System(component_class, is_static)
            self.game._add_system(system)

    def run(self):
        self.awake()
        self.start()
        while self.is_running:
            self.update()
        self.on_destroy()

    def set_ui(self, value):
        self.ui = value

    def get_ui(self):
        return self.ui

    def awake(self):
        for system in self.game.get_systems().values():
            system.awake()

    def start(self):
        for system in self.game.get_systems().values():
            system.start()

    def on_destroy(self):
        for system in self.game.get_systems().values():
            system.on_destroy()
        self.is_running = False
        print(f"{self.name} destroyed")

    def quit(self):
        self.is_running = False

    def update(self):
        for system in self.game.get_systems().values():
            if system.static:
                continue
            system.update()
            # print(f"{system._component_type.__name__} system is updated")

    def add_scene(self, scene, make_current=False):
        self.game.add_scene(scene, make_current)

    def load_scene_from_json(self, scene_json_file, make_current=False):
        with open(scene_json_file) as scene_json:
            scene_dict = json.load(scene_json)
            self.add_scene(Scene.make_from_dict(scene_dict), make_current)

    def set_current_scene(self, scene):
        self.game.set_current_scene(scene)

