from scripts.core.components_base import ComponentsBase
from scripts.core.bounds import Bounds2D, Bounds3D


class Collider2D(ComponentsBase):
    def __init__(self, entity, system, bounds: Bounds2D):
        self.bounds = bounds 
        super().__init__(entity=entity, system=system)

    def __str__(self):
        return f"Collider2D: bounds={self.bounds}"
    
    def __repr__(self):
        return f"Collider2D: bounds={self.bounds}"
    
    def __eq__(self, other: 'Collider2D') -> bool:
        return self.bounds == other.bounds
    
    def __ne__(self, other: 'Collider2D') -> bool:
        return self.bounds != other.bounds
    
    # Collider2D methods including intersect
    def intersect(self, other: 'Collider2D') -> bool:
        return self.bounds.contains(other.bounds.min()) or self.bounds.contains(other.bounds.max())
    
    # Collider2D static methods including create
    @staticmethod
    def create(bounds: Bounds2D):
        return Collider2D(bounds)
    
    # override ComponentsBase methods
    def start(self):
        return super().start()
    
    def update(self):
        return super().update()
    
    def awake(self):
        return super().awake()
    
    def on_destroy(self):
        return super().on_destroy()
    
    def on_disable(self):
        return super().on_disable()
    
    def on_enable(self):
        return super().on_enable()


class Collider3D(ComponentsBase):
    def __init__(self, entity, system, bounds: Bounds3D):
        self.bounds = bounds 
        super().__init__(entity=entity, system=system)

    def __str__(self):
        return f"Collider3D: bounds={self.bounds}"
    
    def __repr__(self):
        return f"Collider3D: bounds={self.bounds}"
    
    def __eq__(self, other: 'Collider3D') -> bool:
        return self.bounds == other.bounds
    
    def __ne__(self, other: 'Collider3D') -> bool:
        return self.bounds != other.bounds
    
    # Collider3D methods including intersect
    def intersect(self, other: 'Collider3D') -> bool:
        return self.bounds.contains(other.bounds.min()) or self.bounds.contains(other.bounds.max())
    
    # Collider3D static methods including create
    @staticmethod
    def create(bounds: Bounds3D):
        return Collider3D(bounds)
    
    # override ComponentsBase methods
    def start(self):
        return super().start()
    
    def awake(self):
        return super().awake()
    
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)
    
    def on_destroy(self):
        return super().on_destroy()
    
    def on_disable(self):
        return super().on_disable()
    
    def on_enable(self):
        return super().on_enable()