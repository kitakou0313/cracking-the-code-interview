import unittest


class Test(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate("1+1"), 2)
        self.assertEqual(calculate("0+4"), 4)
        self.assertEqual(calculate("0*7"), 0)
        self.assertEqual(calculate("9*0+1"), 1)
        self.assertEqual(calculate("1+1+1"), 3)
        self.assertEqual(calculate("1+6/5"), 2)
        self.assertEqual(calculate("3+7/8*7"), 3)
        self.assertEqual(calculate("1+11"), 12)
        self.assertEqual(calculate("200+423"), 623)


if __name__ == "__main__":
    unittest.main()
