import unittest


def getDaysOfAllBlueEyesLeave(numOfBlueEyes):
    if numOfBlueEyes != 0:
        return numOfBlueEyes
    else:
        return 0


class Test(unittest.TestCase):
    def test_getDaysOfAllBlueEyesLeave(self):
        self.assertEqual(getDaysOfAllBlueEyesLeave(5), 5)
        self.assertEqual(getDaysOfAllBlueEyesLeave(6), 6)


if __name__ == "__main__":
    unittest.main()
