from scripts.core.accessor import Accessor
from scripts.core.custom_behavior import CustomBehaviour
from scripts.game.ui.main_dashboard import MainDashboard
from scripts.game.ui.main_menu import MainMenu
from scripts.game.ui.ui_node import UINode


class UserInterface(CustomBehaviour):
    def __init__(self, entity_name, **kwargs):
        super().__init__(entity_name, **kwargs)
        # Set layer to the top of the stack. 32 layers possible make highest layer to be at index 31
        self.layerIndex = kwargs.get("layerIndex", 31)
        self.displayItems = kwargs.get("displayItems", {})
        self.options = kwargs.get("options", [])
        self.main = kwargs.get("main", False)
        self.ui_node: UINode = MainMenu()
        if self.main:
            Accessor.add_accessor("UserInterface", self)
            Accessor.get_accessor("Engine").set_ui(self)

    def awake(self):
        super().awake()

    def start(self):
        super().start()

    def on_enable(self):
        super().on_enable()
    
    def on_disable(self):
        super().on_disable()
    
    def on_destroy(self):
        super().on_destroy()
    
    def update(self, **kwargs):
        super().update(**kwargs)

    @classmethod
    def make_from_dict(cls, entity_name, component_dict):
        return UserInterface(entity_name, **component_dict)
    
    def switch_node(self, next_node):
        self.ui_node = next_node
