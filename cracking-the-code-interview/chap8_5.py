import unittest


def multiplyHelper(smaller, bigger, sumResDec):
    if smaller == 1:
        return bigger

    if (smaller, bigger) in sumResDec:
        return sumResDec[(smaller, bigger)]

    side1 = smaller >> 1
    side1Res = multiplyHelper(side1, bigger, sumResDec)

    side2Res = side1Res

    if smaller & 1 == 1:
        side2Res = multiplyHelper(smaller - side1, bigger, sumResDec)

    sumResDec[(smaller, bigger)] = side1Res + side2Res
    return side1Res + side2Res


def multiply(a, b):
    smaller = min(a, b)
    bigger = max(a, b)

    sumResDec = {}

    return multiplyHelper(smaller, bigger, sumResDec)


class Test(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(1, 125), 125)
        self.assertEqual(multiply(7, 11), 77)
        self.assertEqual(multiply(10000000010, 21), 210000000210)
        self.assertEqual(multiply(33, 100), 3300)


if __name__ == "__main__":
    unittest.main()
