import unittest
import random


def rand5():
    return random.randint(0, 4)


def rand7():
    probably = random.randint(0, 6)
    if probably == 0:
        return 6
    elif probably == 1:
        return 5
    else:
        return rand5()


class Counter(dict):
    def __missing__(self, item):
        return 0


class Test(unittest.TestCase):
    def test_rand7(self):
        talleys = Counter()
        for _ in range(70000):
            talleys[rand7()] += 1
        self.assertEqual(talleys[-1], 0)
        self.assertEqual(talleys[7], 0)
        for i in range(7):
            self.assertTrue(talleys[i] > 9000)
            self.assertTrue(talleys[i] < 11000)


if __name__ == "__main__":
    unittest.main()
