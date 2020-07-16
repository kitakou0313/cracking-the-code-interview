import unittest


def findMatchingPatterns(string, a):


class Test(unittest.TestCase):
    def test_findMatchingPatterns(self):
        self.assertTrue(findMatchingPatterns("dogdogturtledog", "aaba"))
        self.assertTrue(findMatchingPatterns("dogdogturtledog", "bbab"))
        self.assertTrue(findMatchingPatterns("dogdogturtledogdog", "aabaa"))
        self.assertTrue(findMatchingPatterns("dogdogturtledogdog", "aba"))
        self.assertTrue(findMatchingPatterns("dogdogturtledogdo", "aba"))
        self.assertFalse(findMatchingPatterns("dogdogturtledogdg", "aba"))
        self.assertTrue(findMatchingPatterns("catcatbirdbird", "aabb"))
        self.assertFalse(findMatchingPatterns("catcatcatbirdbird", "aabb"))
        self.assertTrue(findMatchingPatterns(
            "buffalobuffalobuffalobuffalo", "aaaa"))
        self.assertFalse(findMatchingPatterns(
            "buffalobuffalouffalobuffalo", "aaaa"))


if __name__ == "__main__":
    unittest.main()
