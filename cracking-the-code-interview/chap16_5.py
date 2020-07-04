import unittest
import math


def count5InNum(num):
    numOf5 = 0
    while num % 5 == 0:
        numOf5 += 1
        num /= 5

    return numOf5


def countNumOf0OnButtom(n):
    numOf5 = 0
    baisuOf5 = 5
    while n >= baisuOf5:
        numOf5 += count5InNum(baisuOf5)
        baisuOf5 += 5

    return numOf5


class Test(unittest.TestCase):
    def test_countNumOf0OnButtom(self):
        self.assertEqual(countNumOf0OnButtom(4), 0)
        self.assertEqual(countNumOf0OnButtom(9), 1)
        self.assertEqual(countNumOf0OnButtom(10), 2)
        self.assertEqual(countNumOf0OnButtom(25), 6)
        self.assertEqual(countNumOf0OnButtom(55), 13)


if __name__ == "__main__":
    unittest.main()
