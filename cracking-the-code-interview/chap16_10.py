import unittest


class Test(unittest.TestCase):
    def test_most_living_people(self):
        people = [P(1907, 1942), P(1909, 1982), P(
            1933, 1967), P(1912, 1954), P(1980), P(1988)]
        self.assertEqual(most_living_people(people), 1933)


if __name__ == "__main__":
    unittest.main()
