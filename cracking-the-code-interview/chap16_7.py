import unittest


def getBiggerNumber(num1, num2):

    k = 0  # num1 > num2の時1になるよ

    hugoNum = num2 - num1

    for i in range(63):
        hugoNum >>= 1

    k = hugoNum & 1

    return k*num1 + (1 - k)*num2


class Test(unittest.TestCase):
    def test_getBiggerNumber(self):
        self.assertEqual(getBiggerNumber(10000, 10), 10000)
        self.assertEqual(getBiggerNumber(0x10000, 0xFFFF), 0x10000)
        self.assertEqual(getBiggerNumber(1212121, 1234567), 1234567)


if __name__ == "__main__":
    unittest.main()
