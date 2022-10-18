import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point with coords {self.x}, {self.y}'
    def get_dist(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return dist

p1 = Point(1, 2)
p2 = Point(1, 0)
dist = p1.get_dist(p2)
print(dist)

