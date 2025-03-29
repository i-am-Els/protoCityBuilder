from scripts.core.custom_behavior import CustomBehaviour


class UserInterface(CustomBehaviour):
    def __init__(self, entity_name, **kwargs):
        super().__init__(entity_name, **kwargs)
        # Set layer to the top of the stack. 32 layers possible make highest layer to be at index 31
        self.layerIndex = kwargs.get("layerIndex", 31)
        self.displayItems = kwargs.get("displayItems", {})
        self.options = kwargs.get("options", [])

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
