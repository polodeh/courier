import unittest
from main import Point

class PointsTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)
    def test_dist_to_center(self):
        point =  Point(2, 0)
        center = Point(0, 0)
        dist = point.get_dist(center)
        self.assertEqual(2, dist)
    def test_bad_init(self):
        point = Point(2, 'o')
        center = Point(0, 0)
        self.assertRaises(TypeError, point.get_dist(center))

