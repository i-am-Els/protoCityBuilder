import json
from game import Game
from scripts.core.scene import Scene
from scripts.core.systems import System
from scripts.core.accessor import Accessor


class Engine:
    def __init__(self, name):
        self.name = name
        self.game = Game()
        self.add_scene(scene=Scene(name="Main"))
        self.set_current_scene(scene=self.game.get_scene(name="Main"))
        self.is_running = True
        self.game._set_quit_callback(self.quit)
        Accessor.add_accessor(name="Engine", obj=self)

    def add_systems(self, systems):
        for system in systems:
            self.game.add_system(system)

    def add_systems_from_classes(self, component_classes):
        for component_class in component_classes:
            system = System(component_class)
            self.game.add_system(system)

    def run(self):
        self.awake()
        self.start()
        while self.is_running:
            for system in self.game.get_systems():
                system.update()
        self.on_destroy()

    def awake(self):
        for system in self.game.get_systems():
            system.awake()

    def start(self):
        for system in self.game.get_systems():
            system.start()

    def on_destroy(self):
        for system in self.game.get_systems():
            system.on_destroy()
        self.is_running = False
        print(f"Engine {self.name} destroyed")

    def quit(self):
        self.is_running = False

    def update(self):
        pass

    def add_scene(self, scene, make_current=False):
        self.game.add_scene(scene, make_current)

    def load_scene_from_json(self, scene_json_file, make_current=False):
        with open(scene_json_file) as scene_json:
            scene_dict = json.load(scene_json)
            self.add_scene(Scene.make_from_dict(scene_dict), make_current)

    def set_current_scene(self, scene):
        self.game.set_current_scene(scene)