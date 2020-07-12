import unittest

# どの直線に属する点が一番多いか考えればいいだけなんだから傾きと切片でハッシュマップ作れば良かった…


class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y


def getBitIndexes(bit):
    bitInd = 0
    indList = []
    while bit != 0:
        if bit & 1 == 1:
            indList.append(bitInd)
        bitInd += 1
        bit >>= 1

    return indList


def isEnableMakeLine(points):
    slope = (points[0].y - points[1].y) / \
        (points[0].x - points[1].x)
    intersect = points[0].y - points[0].x*slope

    def line(x): return slope*x + intersect

    for point in points:
        if line(point.x) != point.y:
            return False
    return True


def calculateBeatLine(pointsList):
    N = len(pointsList)

    ansPointsNum = -1
    slope = 0
    intersection = 0
    for i in range(1, 2 ** N):
        pointsInd = getBitIndexes(i)

        if len(pointsInd) == 1 or len(pointsInd) == 0:
            continue

        points = [pointsList[i]
                  for i in range(len(pointsList)) if i in pointsInd]

        if isEnableMakeLine(points) and len(pointsInd) > ansPointsNum:
            ansPointsNum = len(pointsInd)
            slope = (points[0].y - points[1].y) / \
                (points[0].x - points[1].x)
            intersection = points[0].y - points[0].x*slope

    return lambda x: slope * x + intersection


class Test(unittest.TestCase):
    def test_calculateBeatLine(self):
        points = [Point(0, 0), Point(1, 1), Point(
            2, 2), Point(3, 3), Point(4, 4)]
        line = calculateBeatLine(points)
        self.assertEqual(line(0), 0)
        self.assertEqual(line(1.5), 1.5)
        self.assertEqual(line(10.3), 10.3)
        line = calculateBeatLine(
            [Point(p.x + 0.125, p.y + 5.4) for p in points])
        self.assertEqual(line(0), 5.275)
        self.assertEqual(line(9), 14.275)
        points = [Point(1, 2), Point(2, 1), Point(
            3, 4), Point(4, 5), Point(5, 6)]
        line = calculateBeatLine(points)

        self.assertAlmostEqual(line(1), 2, 14)
        self.assertEqual(line(5), 6)
        points[-1].y = 7
        self.assertAlmostEqual(line(2), 3, 14)


if __name__ == "__main__":
    unittest.main()
