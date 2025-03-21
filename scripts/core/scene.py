class Scene:
    def __init__(self, name):
        self.name = name
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def render(self):
        print(f"Rendering scene {self.name}")
        for entity in self.entities:
            entity.render()

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)

    def get_entity(self, name):
        for entity in self.entities:
            if entity.name == name:
                return entity
            
        return None
    
    def get_entities(self):
        return self.entities
    
    def has_entity(self, name):
        return any(entity.name == name for entity in self.entities)

