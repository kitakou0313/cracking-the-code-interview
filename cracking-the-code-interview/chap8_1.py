import unittest


def getNumOfHowManyStep(step):
    stepsArray = [0 for i in range(step + 1)]
    stepsArray[0] = 1
    for nowStep in range(len(stepsArray)):
        if nowStep + 1 <= step:
            stepsArray[nowStep + 1] += stepsArray[nowStep]

        if nowStep + 2 <= step:
            stepsArray[nowStep + 2] += stepsArray[nowStep]

        if nowStep + 3 <= step:
            stepsArray[nowStep + 3] += stepsArray[nowStep]

    return stepsArray[step]


class Test(unittest.TestCase):
    def test_triple_step(self):
        self.assertEqual(getNumOfHowManyStep(3), 4)
        self.assertEqual(getNumOfHowManyStep(7), 44)


if __name__ == "__main__":
    unittest.main()
