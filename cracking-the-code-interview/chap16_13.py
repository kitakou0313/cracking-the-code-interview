import unittest
import random


class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y


class Square():
    def __init__(self, center, length):
        self.center, length = center, length


def getLineDevidingSquaresEqually(sq1, sq2):

    slope = (sq1.center.y - sq2.center.y) / (sq1.center.x - sq2.center.x)

    intersect = sq1.center.y - sq1.center.x*slope

    return lambda x: slope * x + intersect


class Test(unittest.TestCase):
    def test_getLineDevidingSquaresEqually(self):
        sq1 = Square(Point(2, 4.5), 2)
        sq2 = Square(Point(7, 4.5), 3)
        line = getLineDevidingSquaresEqually(sq1, sq2)
        self.assertEqual(line(0), 4.5)
        self.assertEqual(line(11), 4.5)
        for _ in range(10):
            center1 = Point(random.uniform(-10, 10), random.uniform(-10, 10))
            center2 = Point(random.uniform(-10, 10), random.uniform(-10, 10))
            square1 = Square(center1, random.uniform(
                1, 9))
            square2 = Square(center2, random.uniform(
                1, 9))
            line = getLineDevidingSquaresEqually(square1, square2)
            self.assertAlmostEqual(line(center1.x), center1.y, 7)
            self.assertAlmostEqual(line(center2.x), center2.y, 7)
            mid_x = (center1.x + center2.x) / 2
            mid_y = (center1.y + center2.y) / 2
            self.assertAlmostEqual(line(mid_x), mid_y, 7)


if __name__ == "__main__":
    unittest.main()
