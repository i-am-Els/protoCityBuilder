import math


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y and self.z == value.z
    
    def __ne__(self, value):
        return self.x != value.x or self.y != value.y or self.z != value.z
    
    # Vector3 methods including magnitude, normalize, dot, cross_product, square_magnitude, and distance
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        mag = self.magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def square_magnitude(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def distance(self, other):
        return (self - other).magnitude()
    
    # Vector3 static methods including zero, one, up, down, left, right
    @staticmethod
    def zero():
        return Vector3(0, 0, 0)
    
    @staticmethod
    def one():
        return Vector3(1, 1, 1)
    
    @staticmethod
    def up():
        return Vector3(0, 1, 0)
    
    @staticmethod
    def down():
        return Vector3(0, -1, 0)
    
    @staticmethod
    def left():
        return Vector3(-1, 0, 0)
    
    @staticmethod
    def right():
        return Vector3(1, 0, 0)
    
    @staticmethod
    def forward():
        return Vector3(0, 0, 1)
    
    @staticmethod
    def back():
        return Vector3(0, 0, -1)
    
    @staticmethod
    def lerp(start, end, t):
        t = max(0, min(1, t))
        return start + (end - start) * t
    
    @staticmethod
    def lerp_unclamped(start, end, t):
        return start + (end - start) * t
    
    @staticmethod
    def move_towards(current, target, max_distance_delta):
        distance = target - current
        magnitude = distance.magnitude()
        if magnitude <= max_distance_delta or magnitude == 0:
            return target
        return current + distance / magnitude * max_distance_delta
    
    @staticmethod
    def is_normalized(vector):
        return vector.magnitude() == 1
    
    @staticmethod
    def angle(from_vector, to_vector):
        return math.acos(from_vector.dot(to_vector) / (from_vector.magnitude() * to_vector.magnitude()))
    
    @staticmethod
    def distance(a, b):
        return (a - b).magnitude()
    
    @staticmethod
    def project(vector, on_normal):
        return on_normal * (vector.dot(on_normal) / on_normal.square_magnitude())
    
    @staticmethod
    def project_on_plane(vector, plane_normal):
        return vector - Vector3.project(vector, plane_normal)
    
    @staticmethod
    def reflect(in_direction, in_normal):
        return in_normal * (-2 * in_direction.dot(in_normal)) + in_direction    
    
    @staticmethod
    def angle_between(from_vector, to_vector):
        return math.acos(from_vector.dot(to_vector) / (from_vector.magnitude() * to_vector.magnitude()))
    
    @staticmethod
    def clamp_magnitude(vector, max_length):
        if vector.square_magnitude() > max_length ** 2:
            return vector.normalize() * max_length
        return vector
    
    @staticmethod
    def cross(lhs, rhs):
        return lhs.cross_product(rhs)
    
    # inverseLerp, remap, and rotate methods
    @staticmethod
    def inverse_lerp(a, b, value):
        if a != b:
            return (value - a) / (b - a)
        return 0
    
    @staticmethod
    def remap(a, b, c, d, value):
        return c + (d - c) * ((value - a) / (b - a))
    
    def rotate(self, axis, angle):
        s = math.sin(angle)
        c = math.cos(angle)
        return self * c + axis.cross_product(self) * s + axis * axis.dot(self) * (1 - c)
    

    

