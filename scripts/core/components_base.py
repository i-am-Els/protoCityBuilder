from scripts.core.accessor import Accessor


class ComponentsBase:
    def __init__(self, entity_name, *args, **kwargs):
        self.tag = kwargs.get("tag", "")
        self.entity: str = entity_name

    def __str__(self):
        return f"ComponentsBase: tag={self.tag}"
    
    def __repr__(self):
        return f"ComponentsBase: tag={self.tag}"
    
    def update(self, *args, **kwargs):
        pass

    def start(self):
        pass

    def awake(self):
        system = Accessor.get_accessor("Game").get_system(self.__class__)
        system.add_component(self)

    def on_enable(self):
        pass

    def on_disable(self):
        pass

    def on_destroy(self):
        system = Accessor.get_accessor("Game").get_system(self.__class__)
        system.remove_component(self)

    @classmethod
    def make_from_dict(cls, entity_name, component_dict: dict):
        pass