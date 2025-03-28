# This is the main file of the project. It is the entry point of the application.
# It creates an instance of the Engine class and runs it.
from scripts.core.collider import Collider3D
from scripts.core.engine import Engine
from scripts.core.mesh_renderer import MeshRenderer
from scripts.core.transform import Transform3D
from scripts.core.scene import Scene
from scripts.core.entity import Entity
from scripts.game.user_interface import UserInterface
from scripts.core.component_registry import ComponentsRegistry


class WorldOfTextCraft(Engine):
    def __init__(self, name):
        super().__init__(name=name)
        # Register game defined custom components with component registry so that a system is instantiated for them.
        ComponentsRegistry.add_to_registry_from_dict({"UserInterface": UserInterface})
        # Add required systems through 
        self.add_systems_from_classes({Transform3D: True, MeshRenderer: False, Collider3D: False, UserInterface: True})
        # Add required scenes from the scenes json and in the same process load all entities
        self.load_scene_from_json(scene_json_file="assets/scenes/settlement1.json", make_current=True)


    def awake(self):
        super().awake()
        print("Awake just fired")

    def start(self):
        super().start()
        print("Start just concluded")

    def on_destroy(self):
        super().on_destroy()
        print("on destroy done")

    def update(self):
        super().update()


app = WorldOfTextCraft(name="World of TextCraft")

app.run()
