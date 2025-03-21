# Test cases for vector2.py and vector3.py in scripts/core/native

import unittest
from scripts.core.native.vector2 import Vector2
from scripts.core.native.vector3 import Vector3
import math

class TestVector2(unittest.TestCase):
    def test_add(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        self.assertEqual(v1 + v2, Vector2(4, 6))
    
    def test_sub(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        self.assertEqual(v1 - v2, Vector2(-2, -2))
    
    def test_mul(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        self.assertEqual(v1 * v2, Vector2(3, 8))
    
    def test_truediv(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        self.assertEqual(v1 / v2, Vector2(1/3, 2/4))
    
    def test_eq(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(1, 2)
        self.assertEqual(v1 == v2, True)
    
    def test_ne(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        self.assertEqual(v1 != v2, True)
    
    def test_str(self):
        v1 = Vector2(1, 2)
        self.assertEqual(str(v1), "Vector2(1, 2)")
    
    def test_repr(self):
        v1 = Vector2(1, 2)
        self.assertEqual(repr(v1), "Vector2(1, 2)")
    
    def test_magnitude(self):
        v1 = Vector2(3, 4)
        self.assertEqual(v1.magnitude(), 5)
    
    def test_normalize(self):
        v1 = Vector2(3, 4)
        self.assertEqual(v1.normalize(), Vector2(3/5, 4/5))
    
    def test_dot(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        self.assertEqual(v1.dot(v2), 11)
    
    def test_square_magnitude(self):
        v1 = Vector2(3, 4)
        self.assertEqual(v1.square_magnitude(), 25)
    
    def test_distance(self):
        v1 = Vector2(1, 2)
        v2 = Vector2(4, 6)
        self.assertEqual(v1.distance(v2), 5)

    def test_zero(self):
        self.assertEqual(Vector2.zero(), Vector2(0, 0))

    def test_one(self):
        self.assertEqual(Vector2.one(), Vector2(1, 1))

    def test_up(self):
        self.assertEqual(Vector2.up(), Vector2(0, 1))

    def test_down(self):
        self.assertEqual(Vector2.down(), Vector2(0, -1))

    def test_left(self):
        self.assertEqual(Vector2.left(), Vector2(-1, 0))

    def test_right(self):
        self.assertEqual(Vector2.right(), Vector2(1, 0))


class TestVector3(unittest.TestCase):
    def test_add(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        self.assertEqual(v1 + v2, Vector3(5, 7, 9))
    
    def test_sub(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        self.assertEqual(v1 - v2, Vector3(-3, -3, -3))
    
    def test_mul(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        self.assertEqual(v1 * v2, Vector3(4, 10, 18))
    
    def test_truediv(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        self.assertEqual(v1 / v2, Vector3(1/4, 2/5, 3/6))
    
    def test_eq(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(1, 2, 3)
        self.assertEqual(v1 == v2, True)
    
    def test_ne(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        self.assertEqual(v1 != v2, True)
    
    def test_str(self):
        v1 = Vector3(1, 2, 3)
        self.assertEqual(str(v1), "Vector3(1, 2, 3)")
    
    def test_repr(self):
        v1 = Vector3(1, 2, 3)
        self.assertEqual(repr(v1), "Vector3(1, 2, 3)")
    
    def test_magnitude(self):
        v1 = Vector3(1, 2, 3)
        self.assertEqual(v1.magnitude(), math.sqrt(14))

    def test_normalize(self):
        v1 = Vector3(1, 2, 3)
        self.assertEqual(v1.normalize(), Vector3(1/math.sqrt(14), 2/math.sqrt(14), 3/math.sqrt(14)))

    def test_dot(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        self.assertEqual(v1.dot(v2), 32)

    def test_cross_product(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        self.assertEqual(v1.cross_product(v2), Vector3(-3, 6, -3))

    def test_square_magnitude(self):
        v1 = Vector3(1, 2, 3)
        self.assertEqual(v1.square_magnitude(), 14)

    def test_distance(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 6, 8)
        self.assertEqual(Vector3.distance(v1, v2), math.sqrt(50))

    def test_zero(self):
        self.assertEqual(Vector3.zero(), Vector3(0, 0, 0))
        
    def test_one(self):
        self.assertEqual(Vector3.one(), Vector3(1, 1, 1))

    def test_up(self):
        self.assertEqual(Vector3.up(), Vector3(0, 1, 0))

    def test_down(self):
        self.assertEqual(Vector3.down(), Vector3(0, -1, 0))

    def test_left(self):
        self.assertEqual(Vector3.left(), Vector3(-1, 0, 0))

    def test_right(self):
        self.assertEqual(Vector3.right(), Vector3(1, 0, 0))

if __name__ == "__main__":
    unittest.main()