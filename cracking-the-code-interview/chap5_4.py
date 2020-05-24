import unittest


def getPrev(num):
    c = num
    c0 = 0
    c1 = 0
    while c != 0 and (c & 1) == 1:
        c1 += 1
        c >>= 1
    if c == 0:
        return None
    while c != 0 and (c & 1) == 0:
        c0 += 1
        c >>= 1

    clearedN = num & ((~0) << (c1 + c0 + 1))
    return clearedN | (((1 << (c1 + 1)) - 1) << (c0 - 1))


def getNext(num):
    c = num
    c0 = 0
    while c != 0 and (c & 1) == 0:
        c >>= 1
        c0 += 1
    c1 = 0
    while c != 0 and (c & 1) == 1:
        c >>= 1
        c1 += 1

    cleanedN = (num & ~(2 ** (c1 + c0 + 1) - 1)) | (1 << (c0 + c1))

    return cleanedN | ((1 << (c1 - 1))-1)


def getNearlyNumber(num):
    return (getPrev(num), getNext(num))


class Test(unittest.TestCase):
    def test_getNearlyNumber(self):
        self.assertEqual(getNearlyNumber(8), (4, 16))
        self.assertEqual(getNearlyNumber(12), (10, 17))
        self.assertEqual(getNearlyNumber(15), (None, 23))
        self.assertEqual(getNearlyNumber(143), (124, 151))
        self.assertEqual(getNearlyNumber(159), (126, 175))


if __name__ == "__main__":
    unittest.main()
