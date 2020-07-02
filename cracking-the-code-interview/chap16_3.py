import unittest
import math


class Point():
    def __init__(self, x, y):
        self._x, self._y = x, y

    def getPoint(self):
        return (self._x, self._y)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getDistance(self, other):
        if self.getPoint() == other.getPoint():
            return 0
        else:
            return math.sqrt((other.getPoint()[0] - self.getPoint()[0]) ** 2 + (other.getPoint()[1] - self.getPoint()[1]) ** 2)


class Segment():
    def __init__(self, point1, point2):
        self.start = point1 if point1.getX() <= point2.getX() else point2
        self.end = point2 if point1.getX() <= point2.getX() else point1

        self.slope = (self.end.getY() - self.start.getY()) / \
            (self.end.getX() - self.start.getX())

        self.intersection = self.end.getY() - self.slope * self.end.getX()

    def isInsideSegment(self, point):
        if (self.start.getX() <= point.getX() and self.end.getX() >= point.getX()):
            return (self.start.getY() <= point.getY() and self.end.getY() >= point.getY()) or (self.end.getY() <= point.getY() and self.start.getY() >= point.getY())
        else:
            return False


def findIntersectionPoint(seg1, seg2):

    if seg1.slope == seg2.slope:
        if seg1.intersection == seg2.intersection and seg2.isInsideSegment(seg1.end):
            return seg1.end

        return None

    else:
        posX = (seg2.intersection - seg1.intersection) / \
            (seg1.slope - seg2.slope)

        posY = (seg2.slope * seg1.intersection - seg1.slope *
                seg2.intersection) / (seg2.slope - seg1.slope)

        posPoint = Point(posX, posY)

        if seg1.isInsideSegment(posPoint) and seg2.isInsideSegment(posPoint):
            return posPoint

        else:
            return None


class Test(unittest.TestCase):
    def test_intersection(self):
        seg1 = Segment(Point(1, 1), Point(4, 4))
        seg2 = Segment(Point(3, 3), Point(7, 7))
        self.assertEqual(findIntersectionPoint(seg1, seg2).getPoint(), (4, 4))
        seg1 = Segment(Point(1, 1), Point(4, 4))
        seg2 = Segment(Point(5, 5), Point(8, 8))
        self.assertEqual(findIntersectionPoint(seg1, seg2), None)
        seg1 = Segment(Point(1, 1), Point(4, 4))
        seg2 = Segment(Point(3, -3), Point(-2, 2))
        self.assertEqual(findIntersectionPoint(seg1, seg2), None)
        seg1 = Segment(Point(-1, -1), Point(4, 4))
        seg2 = Segment(Point(3, -3), Point(-2, 2))
        self.assertEqual(findIntersectionPoint(seg1, seg2).getPoint(), (0, 0))
        seg1 = Segment(Point(0, -1), Point(5, 4))
        seg2 = Segment(Point(4, -3), Point(-1, 2))
        self.assertEqual(findIntersectionPoint(seg1, seg2).getPoint(), (1, 0))
        seg1 = Segment(Point(0, 1), Point(5, 6))
        seg2 = Segment(Point(4, -1), Point(-1, 4))
        self.assertEqual(findIntersectionPoint(seg1, seg2).getPoint(), (1, 2))
        seg1 = Segment(Point(0, 1), Point(10, 31))
        seg2 = Segment(Point(0, 4.5), Point(10, 28.5))
        self.assertEqual(findIntersectionPoint(
            seg1, seg2).getPoint(), (5.833333333333332, 18.499999999999996))


if __name__ == "__main__":
    unittest.main()
