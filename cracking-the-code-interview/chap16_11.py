import unittest


def calcurateDivingBoardPossibleHeights(k, shouter, higher):
    possibleHeights = set([])

    for sNums in range(k + 1):
        possibleHeights.add(sNums*shouter + (k - sNums)*higher)

    return sorted(list(possibleHeights))


class Test(unittest.TestCase):
    def test_calcurateDivingBoardPossibleHeights(self):
        self.assertEqual(calcurateDivingBoardPossibleHeights(
            5, 3, 4), [15, 16, 17, 18, 19, 20])
        self.assertEqual(calcurateDivingBoardPossibleHeights(
            4, 2, 6), [8, 12, 16, 20, 24])


if __name__ == "__main__":
    unittest.main()
