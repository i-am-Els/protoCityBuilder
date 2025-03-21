import math
from scripts.core.components_base import ComponentsBase
from scripts.core.native.vector3 import Vector3


class Transform3D(ComponentsBase):
    def __init__(self, entity, system, position, rotation, scale):
        self.position = position
        self.rotation = rotation
        self.scale = scale
        super().__init__(entity=entity, system=system)

    def __str__(self):
        return f"Transform3D: position={self.position}, rotation={self.rotation}, scale={self.scale}"
    
    def __repr__(self):
        return f"Transform3D: position={self.position}, rotation={self.rotation}, scale={self.scale}"
    
    def __eq__(self, other: 'Transform3D') -> bool:
        return self.position == other.position and self.rotation == other.rotation and self.scale == other.scale
    
    def __ne__(self, other: 'Transform3D') -> bool:
        return self.position != other.position or self.rotation != other.rotation or self.scale != other.scale
    
    def translate(self, translation):
        self.position += translation

    def rotate(self, rotation):
        self.rotation += rotation

    def scale(self, scaling):
        self.scale *= scaling

    @staticmethod
    def identity() -> 'Transform3D':
        return Transform3D(Vector3.zero(), Vector3.zero(), Vector3.one())
    
    @property
    def forward(self) -> Vector3:
        return Vector3(math.cos(self.rotation.x) * math.cos(self.rotation.y), math.sin(self.rotation.x), math.cos(self.rotation.x) * math.sin(self.rotation.y))
    
    @property
    def right(self) -> Vector3:
        return Vector3(-math.sin(self.rotation.y), 0, math.cos(self.rotation.y))
    
    @property
    def up(self) -> Vector3:
        return Vector3(math.sin(self.rotation.x) * math.cos(self.rotation.y), -math.cos(self.rotation.x), math.sin(self.rotation.x) * math.sin(self.rotation.y))
    
    def get_forward(self) -> Vector3:
        return self.forward
    
    def get_right(self) -> Vector3:
        return self.right
    
    def get_up(self) -> Vector3:
        return self.up
    
    def look_at(self, target: Vector3):
        direction = (target - self.position).normalize()
        self.rotation.x = math.asin(direction.y)
        self.rotation.y = math.atan2(direction.x, direction.z)
        self.rotation.z = 0

# Transform3D methods including look_at
#     def look_at(self, target: Vector3):
#         direction = (target - self.position).normalize()
#         self.rotation.x = math.asin(direction.y)  # pitch
#         self.rotation.y = math.atan2(direction.x, direction.z)  # yaw
#         self.rotation.z = 0  # roll

# Override methods from ComponentsBase including start, awake, on_enable, on_disable, on_destroy
    def start(self):
        super().start()

    def awake(self):
        super().awake()

    def on_enable(self):
        super().on_enable()

    def on_disable(self):
        super().on_disable()    

    def on_destroy(self):
        super().on_destroy()
