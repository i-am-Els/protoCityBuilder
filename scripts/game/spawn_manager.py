from scripts.core.custom_behavior import CustomBehaviour


class SpawnManager(CustomBehaviour):
    def __init__(self, entity_name, **kwargs):
        super().__init__(entity_name, **kwargs)
        self.resourceType = kwargs.get("resourceType")
        self.gatherRate = kwargs.get("gatherRate")
        self.maxAmount = kwargs.get("maxAmount")
        self.respawnTime = kwargs.get("respawnTime")

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
        return SpawnManager(entity_name, **component_dict)