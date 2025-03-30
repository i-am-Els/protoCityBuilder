from scripts.core.accessor import Accessor
from scripts.game.ui.ui_node import UINode


class GameMap(UINode):
    def __init__(self, parent=None, options=None):
        super().__init__("Show Map", parent, options)
        Accessor.add_accessor("GameMap", self)

    def draw_ui(self, message=None):
        _message = f"You can do a number of things in this world, select items on the map to explore futher..."
        super().draw_ui(_message)
        print(f"Enter the option number...............         or Back[b] | Main Menu [m]")
        self.process_input(["b", "m"])

    def process_input(self, valid_options):
        super().process_input(valid_options)
    # might have to rely on global callbacks for b, q, m and some of the main operations

    def custom_valid_options(self, input_option):
        super().custom_valid_options(input_option)
    
    def index_selection(self, index):
        super().index_selection(index)

    def clear_input(self):
        super().clear_input()

