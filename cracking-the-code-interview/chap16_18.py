import unittest


class Test(unittest.TestCase):
    def test_matches_pattern(self):
        self.assertTrue(matches_pattern("dogdogturtledog", "aaba"))
        self.assertTrue(matches_pattern("dogdogturtledog", "bbab"))
        self.assertTrue(matches_pattern("dogdogturtledogdog", "aabaa"))
        self.assertTrue(matches_pattern("dogdogturtledogdog", "aba"))
        self.assertTrue(matches_pattern("dogdogturtledogdo", "aba"))
        self.assertFalse(matches_pattern("dogdogturtledogdg", "aba"))
        self.assertTrue(matches_pattern("catcatbirdbird", "aabb"))
        self.assertFalse(matches_pattern("catcatcatbirdbird", "aabb"))
        self.assertTrue(matches_pattern(
            "buffalobuffalobuffalobuffalo", "aaaa"))
        self.assertFalse(matches_pattern(
            "buffalobuffalouffalobuffalo", "aaaa"))


if __name__ == "__main__":
    unittest.main()
