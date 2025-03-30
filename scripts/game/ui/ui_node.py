from typing import List
from scripts.core.accessor import Accessor
from scripts.game.node import Node
from scripts.game.ui.main_dashboard import MainDashboard


class UINode(Node):
    def __init__(self, display_text, parent=None, options: List["UINode"]=None):
        super().__init__(display_text=display_text, parent=parent)
        self.display_text = display_text
        self.is_header: False
        self.options: List[UINode | Node] = options or []
        self.parent = parent if parent else []
        
    def draw_ui(self, message):
        MainDashboard.draw_ui()
        print(f"{message}\n")
        option_count = len(self.options)
        if option_count == 1:
            print(f"#{1}. {self.options[0].display_text}\n")
            return
        if option_count == 0:
            print(f"No Save Profile yet, create a new one.")
            return
        for i in range(0, option_count, 2):
            if i + 1 >= option_count:
                print(f"#{i+1}. {self.options[i].display_text}\n")
                break
            print(f"#{i+1}. {self.options[i].display_text}                     {self.options[i+1].display_text}. #{i+2}\n")

    def process_input(self, valid_options: List[str]):
        self.input = input(">>> ")
        try:
            if self.input in valid_options:
                self.custom_valid_options(self.input)
            elif (int(self.input) - 1) < len(self.options):
                self.index_selection(int(self.input) - 1)
            else:
                raise ValueError(f"Input {self.input} not a valid option.")
        except ValueError:
            print("Incorrect Value")
            self.remain()
        except TypeError:
            self.remain()
            print("Cannot cast option input to integer... Did you enter an alphabet? this happens when the alphabet based option doesn't' match any expected option")
        finally:
            self.clear_input()

    def custom_valid_options(self, input_option: str):
        if input_option == "q":
            self.quit()
            return True
        if input_option == "b":
            self.back()
            return True
        if input_option == "m":
            self.main()
            return True
        return False

    def index_selection(self, index: int):
        self.next(self.options[index])

    def clear_input(self):
        self.input = None

    def quit(self):
        Accessor.get_accessor("Engine").quit()

    def back(self):
        Accessor.get_accessor("UserInterface").switch_node(self.parent)

    def main(self):
        Accessor.get_accessor("UserInterface").switch_node(Accessor.get_accessor("MainMenu"))

    def next(self, node: "UINode"):
        Accessor.get_accessor("UserInterface").switch_node(node)

    def remain(self):
        Accessor.get_accessor("UserInterface").switch_node(self)
