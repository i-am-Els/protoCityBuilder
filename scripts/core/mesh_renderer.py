from scripts.core.components_base import ComponentsBase

class MeshRenderer(ComponentsBase):
    def __init__(self, entity_name, mesh=None, material=None, **kwargs):
        super().__init__(entity_name=entity_name, **kwargs)
        self.mesh = mesh if mesh is not None else kwargs.get("mesh", None)
        self.material = material if material is not None else kwargs.get("material", None)

    def __str__(self):
        return f"MeshRenderer: mesh={self.mesh}, material={self.material}"
    
    def __repr__(self):
        return f"MeshRenderer: mesh={self.mesh}, material={self.material}"
    
    def __eq__(self, other: 'MeshRenderer') -> bool:
        return self.mesh == other.mesh and self.material == other.material
    
    def __ne__(self, other: 'MeshRenderer') -> bool:
        return self.mesh != other.mesh or self.material != other.material
    
    # MeshRenderer methods including render
    def render(self):
        print(f"Rendering mesh {self.mesh} with material {self.material}")

    def get_mesh(self):
        return self.mesh
    
    def get_material(self):
        return self.material
    
    def set_mesh(self, mesh):
        self.mesh = mesh

    def set_material(self, material):
        self.material = material
    
    # Override ComponentsBase methods
    def start(self):
        super().start()
    
    def update(self):
        super().update()
    
    def awake(self):
        super().awake()
    
    def on_destroy(self):
        super().on_destroy()
    
    def on_enable(self):
        super().on_enable()
    
    def on_disable(self):
        super().on_disable()   

    @classmethod
    def make_from_dict(cls, entity_name, component_dict):
        return cls(entity_name, **component_dict)
