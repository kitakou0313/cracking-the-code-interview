import unittest


def paint_fill_hepler(image, x, y, originColor, targetColor):
    X = len(image[0])
    Y = len(image)

    image[y][x] = targetColor

    dvecs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    for dvec in dvecs:
        if x + dvec[0] < X and 0 <= x + dvec[0] and y + dvec[1] < Y and 0 <= y + dvec[1] and image[y + dvec[1]][x + dvec[0]] == originColor:
            paint_fill_hepler(
                image, x + dvec[0], y + dvec[1], originColor, targetColor)


def paint_fill(image, x, y, color):
    X = len(image[0])
    Y = len(image)

    originColor = image[y][x]

    image[y][x] = color

    dvecs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    for dvec in dvecs:
        if x + dvec[0] < X and 0 <= x + dvec[0] and y + dvec[1] < Y and 0 <= y + dvec[1] and image[y + dvec[1]][x + dvec[0]] == originColor:
            paint_fill_hepler(
                image, x + dvec[0], y + dvec[1], originColor, color)


class Test(unittest.TestCase):
    def test_paint_fill(self):
        image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
                  [30, 20, 20, 10, 10, 40, 40, 40],
                  [10, 10, 20, 20, 10, 10, 10, 10],
                  [10, 10, 30, 20, 20, 20, 20, 10],
                  [40, 40, 10, 10, 10, 10, 10, 10]]
        image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
                  [30, 20, 20, 30, 30, 40, 40, 40],
                  [10, 10, 20, 20, 30, 30, 30, 30],
                  [10, 10, 30, 20, 20, 20, 20, 30],
                  [40, 40, 30, 30, 30, 30, 30, 30]]
        image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
                  [30, 20, 20, 30, 30, 40, 40, 40],
                  [30, 30, 20, 20, 30, 30, 30, 30],
                  [30, 30, 30, 20, 20, 20, 20, 30],
                  [40, 40, 30, 30, 30, 30, 30, 30]]
        paint_fill(image1, 3, 1, 30)
        self.assertEqual(image1, image2)
        paint_fill(image1, 3, 1, 10)
        paint_fill(image1, 3, 1, 30)
        self.assertEqual(image1, image3)


if __name__ == "__main__":
    unittest.main()
