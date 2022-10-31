import math

from point import Point

if __name__ == '__main__':
    p1 = Point(1, 2)
    print(p1)
    p2 = Point(2, 3)
    print(p2)
    dist = p1.get_dist(p2)
    print(dist)


