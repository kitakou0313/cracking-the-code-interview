import unittest


def selectMostVictoryGame(accuracy):
    winRateOfSingleShot = accuracy

    winRateOfThreeShots = (3 * (accuracy ** 2) *
                           (1-accuracy)) + (accuracy ** 3)

    return "single shot" if winRateOfSingleShot >= winRateOfThreeShots else "three shots"


class Test(unittest.TestCase):
    def test_selectMostVictoryGame(self):
        accuracy = 0
        while accuracy <= 1:
            if accuracy >= accuracy ** 3 + 3 * accuracy ** 2 * (1 - accuracy):
                self.assertEqual(selectMostVictoryGame(
                    accuracy), "single shot")
            else:
                self.assertEqual(selectMostVictoryGame(
                    accuracy), "three shots")
            accuracy += 0.01


if __name__ == "__main__":
    unittest.main()
