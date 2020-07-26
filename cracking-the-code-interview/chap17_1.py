import unittest
import ctypes


def addWithoutPlus(num1, num2):
    sumRes = num1 ^ num2
    carryBit = num1 & num2

    if carryBit == 0:
        return sumRes

    carryBit = (carryBit << 1) & 0x1FFFFFFFFFFFFFFFF
    if carryBit & (1 << 64):
        return ctypes.c_long(sumRes).value  # for overflow
    return addWithoutPlus(carryBit, sumRes)


class Test(unittest.TestCase):
    def test_addWithoutPlus(self):
        self.assertEqual(addWithoutPlus(1, 1), 2)
        self.assertEqual(addWithoutPlus(1, 2), 3)
        self.assertEqual(addWithoutPlus(1001, 234), 1235)
        self.assertEqual(addWithoutPlus(5, -1), 4)
        self.assertEqual(addWithoutPlus(7, -5), 2)
        self.assertEqual(addWithoutPlus(7, -29), -22)
        self.assertEqual(addWithoutPlus(-2, 10), 8)


if __name__ == "__main__":
    unittest.main()
