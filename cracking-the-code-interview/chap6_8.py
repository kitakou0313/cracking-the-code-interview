import unittest
import math


def egg_drop_floor(numOfFloor):
    return math.ceil(0.5 * (math.sqrt(1 + 4 * 2*numOfFloor) - 1))


class Test(unittest.TestCase):
    def test_egg_drop_floor(self):
        self.assertEqual(egg_drop_floor(100), 14)
        self.assertEqual(egg_drop_floor(200), 20)
        self.assertEqual(egg_drop_floor(500), 32)
        self.assertEqual(egg_drop_floor(1000), 45)


if __name__ == "__main__":
    unittest.main()
