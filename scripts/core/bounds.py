class Bounds2D:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Bounds2D(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height
    
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.width != other.width or self.height != other.height
    
    # Bounds2D methods including center, size, min, max, and contains
    def center(self):
        return (self.x + self.width / 2, self.y + self.height / 2)
    
    def size(self):
        return (self.width, self.height)
    
    def min(self):
        return (self.x, self.y)
    
    def max(self):
        return (self.x + self.width, self.y + self.height)
    
    def contains(self, other):
        return self.x <= other.x and self.y <= other.y and self.x + self.width >= other.x + other.width and self.y + self.height >= other.y + other.height
    
    # Bounds2D static methods including zero, one
    @staticmethod
    def zero():
        return Bounds2D(0, 0, 0, 0)
    
    @staticmethod
    def one():
        return Bounds2D(1, 1, 1, 1)
    
    @classmethod
    def from_min_max(cls, min_x, min_y, max_x, max_y):
        width = max_x - min_x
        height = max_y - min_y
        return cls(min_x, min_y, width, height)

class Bounds3D:
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth

    def __repr__(self):
        return f"Bounds3D(x={self.x}, y={self.y}, z={self.z}, width={self.width}, height={self.height}, depth={self.depth})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.width == other.width and self.height == other.height and self.depth == other.depth
    
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z or self.width != other.width or self.height != other.height or self.depth != other.depth
    
    # Bounds3D methods including center, size, min, max, and contains
    def center(self):
        return (self.x + self.width / 2, self.y + self.height / 2, self.z + self.depth / 2)
    
    def size(self):
        return (self.width, self.height, self.depth)
    
    def min(self):
        return (self.x, self.y, self.z)
    
    def max(self):
        return (self.x + self.width, self.y + self.height, self.z + self.depth)
    
    def contains(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z and self.x + self.width >= other.x + other.width and self.y + self.height >= other.y + other.height and self.z + self.depth >= other.z + other.depth
    
    # Bounds3D static methods including zero, one
    @staticmethod
    def zero():
        return Bounds3D(0, 0, 0, 0, 0, 0)
    
    @staticmethod
    def one():
        return Bounds3D(1, 1, 1, 1, 1, 1)
    
    @classmethod
    def from_min_max(cls, min_x, min_y, min_z, max_x, max_y, max_z):
        width = max_x - min_x
        height = max_y - min_y
        depth = max_z - min_z
        return cls(min_x, min_y, min_z, width, height, depth)

    
    