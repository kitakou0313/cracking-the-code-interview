import unittest


def getNumOf1Bit(a):
    tmp = a
    cnt = 0
    while tmp != 0:
        if tmp & 1 == 1:
            cnt += 1
        tmp >>= 1
    return cnt


def countDifferentBits(a, b):
    difBits = a ^ b
    return getNumOf1Bit(difBits)


class Test(unittest.TestCase):
    def test_countDifferentBits(self):
        self.assertEqual(countDifferentBits(16, 2), 2)
        self.assertEqual(countDifferentBits(17, 34), 4)
        self.assertEqual(countDifferentBits(15, 97), 5)

    def test_countDifferentBits(self):
        self.assertEqual(countDifferentBits(16, 2), 2)
        self.assertEqual(countDifferentBits(17, 34), 4)
        self.assertEqual(countDifferentBits(15, 97), 5)


if __name__ == "__main__":
    unittest.main()
