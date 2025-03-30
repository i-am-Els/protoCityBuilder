from scripts.core.accessor import Accessor
from scripts.game.ui.about_ui import AboutUI
from scripts.game.ui.game_map import GameMap
from scripts.game.ui.quest_display import QuestDisplay
from scripts.game.ui.save_ui import SaveUI
from scripts.game.ui.ui_node import UINode


class MainMenu(UINode):
    def __init__(self, parent=None, options=None):
        super().__init__("Main Menu", parent, options)
        self.options = [ QuestDisplay(parent=self), GameMap(parent=self), SaveUI(parent=self), AboutUI(parent=self)]
        Accessor.add_accessor("MainMenu", self)

    def draw_ui(self, message=None):
        _message = "Dear Warrior, What are you up to?"
        super().draw_ui(_message)
        print(f"Enter the option number...............         or Quit[q]")
        self.process_input(["q"])
        
    def process_input(self, valid_options):
        super().process_input(valid_options)

    def custom_valid_options(self, input_option):
        super().custom_valid_options(input_option)        
    
    def index_selection(self, index):
        super().index_selection(index)

    def clear_input(self):
        super().clear_input()
        
    