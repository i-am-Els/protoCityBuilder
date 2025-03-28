from scripts.core.collider import Collider2D, Collider3D
from scripts.core.custom_behavior import CustomBehaviour
from scripts.core.mesh_renderer import MeshRenderer
from scripts.core.transform import Transform2D, Transform3D


class ComponentsRegistry:
    __default_component_registry = {
        "Collider2D": Collider2D,
        "Collider3D": Collider3D,
        "Transform3D": Transform3D,
        "Transform2D": Transform2D,
        "MeshRenderer": MeshRenderer,
        # Add every other engine component classes you make here
    }
    
    def __init__(self):
        pass

    @classmethod
    def component_registy(cls):
        return ComponentsRegistry.__default_component_registry
    
    @classmethod
    def add_to_registry_from_dict(cls, components_dict):
        ComponentsRegistry.__default_component_registry.update(components_dict)
    