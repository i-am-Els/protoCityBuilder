from scripts.core.components_base import ComponentsBase
from scripts.core.bounds import Bounds2D, Bounds3D


class Collider2D(ComponentsBase):
    def __init__(self, entity_name, bounds=None, **kwargs):
        super().__init__(entity_name=entity_name, **kwargs)
        if bounds:
            self.bounds = bounds
        else:
            min_coords = kwargs.get("min")
            max_coords = kwargs.get("max")
            if min_coords and max_coords:
                self.bounds = Bounds2D.from_min_max(*min_coords, *max_coords)
            else:
                raise ValueError("Either 'bounds' or 'min' and 'max' must be provided")
            
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
        super().start()
    
    def update(self):
        super().update()
    
    def awake(self):
        super().awake()
    
    def on_destroy(self):
        super().on_destroy()
    
    def on_disable(self):
        super().on_disable()
    
    def on_enable(self):
        super().on_enable()
    
    @classmethod
    def make_from_dict(cls, entity_name, component_dict):
        return cls(entity_name, **component_dict)


class Collider3D(ComponentsBase):
    def __init__(self, entity_name, bounds=None, **kwargs):
        super().__init__(entity_name=entity_name, **kwargs)
        if bounds:
            self.bounds = bounds
        else:
            min_coords = kwargs.get("min")
            max_coords = kwargs.get("max")
            if min_coords and max_coords:
                self.bounds = Bounds3D.from_min_max(*min_coords, *max_coords)
            else:
                raise ValueError("Either 'bounds' or 'min' and 'max' must be provided")
            
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
        super().start()
    
    def awake(self):
        super().awake()
    
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
    
    def on_destroy(self):
        super().on_destroy()
    
    def on_disable(self):
        super().on_disable()
    
    def on_enable(self):
        super().on_enable()
    
    @classmethod
    def make_from_dict(cls, entity_name, component_dict):
        return cls(entity_name, **component_dict)