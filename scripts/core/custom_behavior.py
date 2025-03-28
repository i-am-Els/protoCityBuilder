from scripts.core.components_base import ComponentsBase


class CustomBehaviour(ComponentsBase):
    def __init__(self, entity_name, **kwargs):
        super().__init__(entity_name=entity_name, **kwargs)

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
        return cls(entity_name, **component_dict)