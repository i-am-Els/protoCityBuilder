# This is the main file of the project. It is the entry point of the application.
# It creates an instance of the Engine class and runs it.
from scripts.core.collider import Collider3D
from scripts.core.engine import Engine
from scripts.core.mesh_renderer import MeshRenderer
from scripts.core.transform import Transform3D
from scripts.core.scene import Scene
from scripts.core.entity import Entity


class WorldOfTextCraft(Engine):
    def __init__(self, name):
        super().__init__(name=name)
        # Add required systems
        self.add_systems_from_classes([Transform3D, MeshRenderer, Collider3D])
        # Add required scenes
        self.load_scene_from_json(scene_json_file="assets/scenes/settlement1.json", make_current=True)
        # Add required entities
        self.game.get_current_scene().add_entity(Entity.make_from_dict())


    def awake(self):
        super().awake()

    def start(self):
        super().start()

    def on_destroy(self):
        super().on_destroy()

    def update(self):
        ...


app = WorldOfTextCraft(name="World of TextCraft")

app.run()
