import unittest

ODDMASK = 0xAAAAAAAAAAAAAAAA
EVENMASK = 0x5555555555555555


def swapOddAndEvenBits(a):
    oddBits = a & ODDMASK
    evenBits = a & EVENMASK

    return (oddBits >> 1) | (evenBits << 1)


class Test(unittest.TestCase):
    def test_swapOddAndEvenBits(self):
        self.assertEqual(swapOddAndEvenBits(42), 21)
        self.assertEqual(swapOddAndEvenBits(21), 42)
        self.assertEqual(swapOddAndEvenBits(43), 23)
        self.assertEqual(swapOddAndEvenBits(511), 767)
        self.assertEqual(swapOddAndEvenBits(1023), 1023)


if __name__ == "__main__":
    unittest.main()
