from scripts.game.ui.ui_node import UINode


class AboutUI(UINode):
    def __init__(self, parent=None, options = None):
        super().__init__("How to Play/About", parent, options)

    def draw_ui(self, message=None):
        _message = f"Dear Warrior,\nThis is World of TextCraft, you are on strict business\n to build an army and a kingdom, lead men to war and \nprotect the people with all you've got, the tales of you victory\n will forever be told.\n\nYour faithful general.\nCaleb of Judah."
        super().draw_ui(_message)
        print(f"Go Back[b] | Quit[q]")
        self.process_input(["b", "q"])

    def process_input(self, valid_options):
        super().process_input(valid_options)

    def custom_valid_options(self, input_option):
        super().custom_valid_options(input_option)
    
    def index_selection(self, index):
        super().index_selection(index)

    def clear_input(self):
        super().clear_input()