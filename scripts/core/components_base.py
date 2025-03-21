class ComponentsBase:
    def __init__(self, entity, system, *args, **kwargs):
        self.tag = kwargs.get("tag", "")
        self.entity = None
        self.__system = system

    def __str__(self):
        return f"ComponentsBase: tag={self.tag}"
    
    def __repr__(self):
        return f"ComponentsBase: tag={self.tag}"
    
    def update(self, *args, **kwargs):
        pass

    def start(self):
        pass

    def awake(self):
        self.__system.add_component(self)

    def on_enable(self):
        pass

    def on_disable(self):
        pass

    def on_destroy(self):
        self.__system.remove_component(self)