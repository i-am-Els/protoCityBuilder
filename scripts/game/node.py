class Node:
    def __init__(self, display_text=None, parent=None):
        self.display_text: str = display_text
        self.parent: Node = parent

    def set_display_text(self, value):
        self.display_text = value

    def set_parent(self, other: "Node"):
        self.parent = other