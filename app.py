# This is the main file of the project. It is the entry point of the application.
# It creates an instance of the Engine class and runs it.
from scripts.core.collider import Collider3D
from scripts.core.component_registry import ComponentsRegistry
from scripts.core.engine import Engine, clear_screen
from scripts.core.mesh_renderer import MeshRenderer
from scripts.core.transform import Transform3D
from scripts.game.spawn_manager import SpawnManager
from scripts.game.user_interface import UserInterface


class WorldOfTextCraft(Engine):
    def __init__(self, name):
        super().__init__(name=name)
        clear_screen("Welcome to World of TextCraft")
        # Register game defined custom components with component registry so that a system is instantiated for them.
        ComponentsRegistry.add_to_registry_from_dict({"UserInterface": UserInterface, "SpawnManager": SpawnManager})
        # Add required systems through 
        self.add_systems_from_classes({Transform3D: True, MeshRenderer: False, Collider3D: False, UserInterface: True, SpawnManager: False})
        # Add required scenes from the scenes json and in the same process load all entities
        self.load_scene_from_json(scene_json_file="assets/scenes/settlement1.json", make_current=True)


    def awake(self):
        clear_screen("Welcome to World of TextCraft")
        super().awake()

    def start(self):
        super().start()

    def on_destroy(self):
        super().on_destroy()

    def update(self):
        super().update()


app = WorldOfTextCraft(name="World of TextCraft")

app.run()
