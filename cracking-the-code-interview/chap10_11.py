import unittest


class Test(unittest.TestCase):
    def test_peaks_and_valleys(self):
        a = [12, 6, 3, 1, 0, 14, 13, 20, 22, 10]
        peaks_and_valleys(a)
        self.assertEqual(a, [6, 12, 1, 3, 0, 14, 13, 22, 10, 20])
        b = [34, 55, 60, 65, 70, 75, 85, 10, 5, 16]
        peaks_and_valleys(b)
        self.assertEqual(b, [34, 60, 55, 70, 65, 85, 10, 75, 5, 16])


if __name__ == "__main__":
    unittest.main()
