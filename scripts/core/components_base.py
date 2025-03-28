from scripts.core.accessor import Accessor


class ComponentsBase:
    def __init__(self, entity_name, **kwargs):
        self.tag = kwargs.get("tag", "")
        self.entity: str = entity_name
        print(f"Component of type {self.__class__.__name__} belonging to {self.entity} initialized")

    def __str__(self):
        return f"ComponentsBase: tag={self.tag}"
    
    def __repr__(self):
        return f"ComponentsBase: tag={self.tag}"
    
    def update(self, **kwargs) -> None:
        pass

    def start(self) -> None:
        pass

    def awake(self) -> None:
        system = Accessor.get_accessor("Game").get_system(self.__class__)
        system.add_component(self)

    def on_enable(self) -> None:
        pass

    def on_disable(self) -> None:
        pass

    def on_destroy(self) -> None:
        system = Accessor.get_accessor("Game").get_system(self.__class__)
        system.remove_component(self)

    @classmethod
    def make_from_dict(cls, entity_name, component_dict: dict):
        pass