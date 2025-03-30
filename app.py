import threading
import time
from scripts.core.engine import Engine
from scripts.core.component_registry import ComponentsRegistry
from scripts.core.transform import Transform3D
from scripts.core.mesh_renderer import MeshRenderer
from scripts.core.collider import Collider3D
from scripts.game.spawn_manager import SpawnManager
from scripts.game.user_interface import UserInterface


class WorldOfTextCraft(Engine):
    def __init__(self, name):
        super().__init__(name=name)
        self.ui_thread = None
        self.ui_running = False

        # Register game-defined custom components
        ComponentsRegistry.add_to_registry_from_dict({"UserInterface": UserInterface, "SpawnManager": SpawnManager})
        self.add_systems_from_classes({Transform3D: True, MeshRenderer: False, Collider3D: False, UserInterface: True, SpawnManager: False})
        self.load_scene_from_json(scene_json_file="assets/scenes/settlement1.json", make_current=True)

    def awake(self):
        self.ui = self.get_ui()
        super().awake()

    def start(self):
        super().start()
        self.start_ui_thread()

    def update(self):
        # Run background tasks in the main thread
        super().update()
        current_time = time.time()
        delta_time = current_time - getattr(self, '_last_frame_time', current_time)
        self._last_frame_time = current_time

        # Use delta_time for frame-dependent updates (e.g., entity translations)
        time.sleep(max(0, 0.1 - delta_time))  # Maintain a consistent frame rate of ~10 FPS

    def on_destroy(self):
        self.stop_ui_thread()
        super().on_destroy()

    def start_ui_thread(self):
        """Start the UI loop in a separate thread."""
        self.ui_running = True
        self.ui_thread = threading.Thread(target=self.ui_loop, daemon=True)
        self.ui_thread.start()

    def stop_ui_thread(self):
        """Stop the UI loop."""
        self.ui_running = False
        if self.ui_thread:
            self.ui_thread.join()

    def ui_loop(self):
        """The UI loop running in a separate thread."""
        while self.ui_running:
            if self.ui and self.ui.ui_node:
                self.ui.ui_node.draw_ui()
            time.sleep(0.5)  # Adjust the sleep time to control UI refresh rate


# Entry point
app = WorldOfTextCraft(name="World of TextCraft")
app.run()
