import math
from scripts.core.components_base import ComponentsBase
from scripts.core.native.vector2 import Vector2
from scripts.core.native.vector3 import Vector3


class Transform2D(ComponentsBase):
    def __init__(self, entity_name, position=Vector2.zero(), angle=0, scale=Vector2.one()):
        self.position = position
        self.angle = angle
        self.scale = scale
        super().__init__(entity_name=entity_name)

    def __str__(self):
        return f"Transform2D: position={self.position}, angle={self.angle}, scale={self.scale}"
    
    def __repr__(self):
        return f"Transform2D: position={self.position}, angle={self.angle}, scale={self.scale}"
    
    def __eq__(self, other: 'Transform2D') -> bool:
        return self.position == other.position and self.angle == other.angle and self.scale == other.scale
    
    def __ne__(self, other: 'Transform2D') -> bool:
        return self.position != other.position or self.angle != other.angle or self.scale != other.scale
    
    # Transform2D methods including translate, rotate, and scale
    def translate(self, translation: Vector2):
        self.position += translation

    def rotate(self, rotation: float):
        self.angle += rotation

    def scale(self, scaling: Vector2):
        self.scale *= scaling

    # Transform2D static methods including identity
    @staticmethod
    def identity() -> 'Transform2D':
        return Transform2D()
    
    # Transform2D properties including forward, right, up
    @property
    def forward(self) -> Vector2:
        return Vector2(math.cos(self.angle), math.sin(self.angle))
    
    @property
    def right(self) -> Vector2:
        return Vector2(-math.sin(self.angle), math.cos(self.angle))
    
    @property
    def up(self) -> Vector2:
        return Vector2(0, 1).rotate(self.angle)
    
    # Transform2D methods including get_forward, get_right, get_up
    def get_forward(self) -> Vector2:
        return self.forward
    
    def get_right(self) -> Vector2:
        return self.right
    
    def get_up(self) -> Vector2:
        return self.up
    
    # Transform2D methods including set_forward, set_right, set_up
    def set_forward(self, forward: Vector2):
        self.angle = math.atan2(forward.y, forward.x)

    def set_right(self, right: Vector2):
        self.angle = math.atan2(-right.x, right.y)

    def set_up(self, up: Vector2):
        self.angle = math.atan2(up.x, up.y)

    # Transform2D methods including get_position, get_angle, get_scale
    def get_position(self) -> Vector2:
        return self.position
    
    def get_angle(self) -> float:
        return self.angle
    
    def get_scale(self) -> Vector2:
        return self.scale
    
    # Transform2D methods including set_position, set_angle, set_scale
    def set_position(self, position: Vector2):
        self.position = position

    def set_angle(self, angle: float):
        self.angle = angle

    def set_scale(self, scale: Vector2):
        self.scale = scale

    # Transform2D methods including look_at
    def look_at(self, target: Vector2):
        direction = (target - self.position).normalize()
        self.angle = math.atan2(direction.y, direction.x)

    # Transform2D methods including move_towards
    def move_towards(self, target: Vector2, max_distance_delta: float) -> Vector2:
        distance = target - self.position
        magnitude = distance.magnitude()
        if magnitude <= max_distance_delta or magnitude == 0:
            return target
        return self.position + distance / magnitude * max_distance_delta
    
    # Override ComponentsBase methods including update, start, awake, on_enable, on_disable, on_destroy
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

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

    @classmethod
    def make_from_dict(cls, entity_name, component_dict):
        return cls(entity_name, Vector2(*component_dict["position"]), component_dict["angle"], Vector2(*component_dict["scale"]))


class Transform3D(ComponentsBase):
    def __init__(self, entity_name, position: Vector3, rotation: Vector3, scale: Vector3):
        self.position = position
        self.rotation = rotation
        self.scale = scale
        super().__init__(entity_name=entity_name)

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

    @classmethod
    def make_from_dict(cls, entity_name, component_dict):
        return cls(entity_name, Vector3(*component_dict["position"]), Vector3(*component_dict["rotation"]), Vector3(*component_dict["scale"]))