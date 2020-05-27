import unittest


class Bottle():
    def __init__(self, weight=1.0):
        self.pillWeight = weight


def findHeavyBottle(bottles):
    sumButtom = 0.5 * (1 + 20) * 20

    sumOfPills = 0
    for i in range(1, 21):
        sumOfPills += bottles[i-1].pillWeight * i

    return int(10 * (sumOfPills - sumButtom)) - 1


class Test(unittest.TestCase):
    def test_findHeavyBottle(self):
        bottles = [Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
                   Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
                   Bottle(), Bottle(), Bottle(), Bottle(), Bottle(1.1),
                   Bottle(), Bottle(), Bottle(), Bottle(), Bottle()]
        self.assertEqual(findHeavyBottle(bottles), 14)


if __name__ == "__main__":
    unittest.main()
