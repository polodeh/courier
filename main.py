class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point with coords {self.x}, {self.y}'
p1 = Point(1, 2)
print(p1)

