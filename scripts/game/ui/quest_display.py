from scripts.core.accessor import Accessor
from scripts.game.ui.ui_node import UINode


class QuestDisplay(UINode):
    def __init__(self, parent=None, options=None):
        super().__init__("View Quests", parent, options)
        Accessor.add_accessor("QuestDisplay", self)

    def draw_ui(self, message=None):
        _message = f"Warrior, these are the Quests awaiting your attention."
        if len(self.options) == 0:
            _message = "Apparently, there are no quests for you, Dear Warrior.\n"
        super().draw_ui(_message)
        print(f"Enter the option number...............         or Go Back[b]")
        self.process_input(["b"])

    def process_input(self, valid_options):
        super().process_input(valid_options)

    def custom_valid_options(self, input_option):
        super().custom_valid_options(input_option)
    
    def index_selection(self, index):
        super().index_selection(index)

    def clear_input(self):
        super().clear_input()