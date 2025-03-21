import math


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x / other.x, self.y / other.y)

    def __eq__(self, other: 'Vector2') -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: 'Vector2') -> bool:
        return self.x != other.x or self.y != other.y

    def __str__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
    
    # Vector2 methods including magnitude, normalize, dot, square_magnitude, and distance
    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self) -> 'Vector2':
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag)
    
    def dot(self, other: 'Vector2') -> float:
        return self.x * other.x + self.y * other.y
    
    def square_magnitude(self) -> float:
        return self.x ** 2 + self.y ** 2
    
    def distance(self, other: 'Vector2') -> float:
        return (self - other).magnitude()
    
    # Vector2 static methods including zero, one, up, down, left, right
    @staticmethod
    def zero() -> 'Vector2':
        return Vector2(0, 0)
    
    @staticmethod
    def one() -> 'Vector2':
        return Vector2(1, 1)
    
    @staticmethod
    def up() -> 'Vector2':
        return Vector2(0, 1)
    
    @staticmethod
    def down() -> 'Vector2':
        return Vector2(0, -1)
    
    @staticmethod
    def left() -> 'Vector2':
        return Vector2(-1, 0)
    
    @staticmethod
    def right() -> 'Vector2':
        return Vector2(1, 0)
    
    # Vector2 class methods including isNormalized, lerp, slerp, and move_towards
    @classmethod
    def isNormalized(cls, vector: 'Vector2') -> bool:
        return vector.magnitude() == 1
    
    @classmethod
    def lerp(cls, a: 'Vector2', b: 'Vector2', t: float) -> 'Vector2':
        return a + (b - a) * t
    
    @classmethod
    def slerp(cls, a: 'Vector2', b: 'Vector2', t: float) -> 'Vector2':
        dot = a.dot(b)
        dot = max(-1, min(dot, 1))
        theta = math.acos(dot) * t
        relative = (b - a * dot).normalize()
        return a * math.cos(theta) + relative * math.sin(theta)
    
    @classmethod
    def move_towards(cls, current: 'Vector2', target: 'Vector2', max_distance_delta: float) -> 'Vector2':
        distance = target - current
        magnitude = distance.magnitude()
        if magnitude <= max_distance_delta or magnitude == 0:
            return target
        return current + distance / magnitude * max_distance_delta
    
    # Vector2 instance methods including inverseLerp, remap, and rotate
    def inverseLerp(self, a: 'Vector2', b: 'Vector2') -> float:
        return (self - a).magnitude() / (b - a).magnitude()
    
    def remap(self, a1: 'Vector2', b1: 'Vector2', a2: 'Vector2', b2: 'Vector2') -> 'Vector2':
        return a2 + (self - a1) * (b2 - a2) / (b1 - a1)
    
    def rotate(self, angle: float) -> 'Vector2':
        angle = math.radians(angle)
        return Vector2(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle)
        )
    
    # Vector2 magic methods including __neg__, __abs__, __round__, __floor__, __ceil__, and __trunc__
    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)
    
    def __abs__(self) -> 'Vector2':
        return Vector2(abs(self.x), abs(self.y))
    
    def __round__(self, n: int = 0) -> 'Vector2':
        return Vector2(round(self.x, n), round(self.y, n))
    
    def __floor__(self) -> 'Vector2':
        return Vector2(math.floor(self.x), math.floor(self.y))
    
    def __ceil__(self) -> 'Vector2':
        return Vector2(math.ceil(self.x), math.ceil(self.y))
    
    def __trunc__(self) -> 'Vector2':
        return Vector2(math.trunc(self.x), math.trunc(self.y))
    