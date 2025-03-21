from scripts.core.collider import Collider2D, Collider3D
from scripts.core.mesh_renderer import MeshRenderer
from scripts.core.transform import Transform2D, Transform3D

component_registry = {
    "Collider2D": Collider2D,
    "Collider3D": Collider3D,
    # Add other component classes here
    "Transform3D": Transform3D,
    "Transform2D": Transform2D,
    "MeshRenderer": MeshRenderer,

}