import unittest


class TestCase():
    def __init__(self, poisonedInd, caseSize):
        class Bottle():
            def __init__(self, isPoisoned):
                self.__isPoisoned = isPoisoned

            def isPoisoned(self):
                return self.__isPoisoned
        self.caseSize = caseSize
        self.bottles = [Bottle(True) if ind == poisonedInd else Bottle(
            False) for ind in range(caseSize)]


class TestPaper():
    def __init__(self):
        self.__testedBottle = None
        self.__testResult = False

    def checkPoison(self, bottle):
        if self.__testResult == True:
            return
        self.__testResult = bottle.isPoisoned()

    def getResult(self):
        return self.__testResult


def findPoisonedBottle(testCase):
    papers = [TestPaper() for i in range(100)]

    for bottleNum in range(1, len(testCase.bottles) + 1):
        tmpInd = bottleNum
        paperInd = 0
        while tmpInd != 0:
            if tmpInd & 1 == 1:
                papers[paperInd].checkPoison(testCase.bottles[bottleNum-1])
            paperInd += 1
            tmpInd >>= 1
    ans = 0
    for paperInd in range(len(papers)):
        if papers[paperInd].getResult():
            ans += 2 ** paperInd

    return ans-1


class Test(unittest.TestCase):
    def test_findPoisonedBottle(self):
        self.assertEqual(findPoisonedBottle(TestCase(0, 1000)), 0)
        self.assertEqual(findPoisonedBottle(TestCase(10, 1000)), 10)
        self.assertEqual(findPoisonedBottle(TestCase(100, 1000)), 100)
        self.assertEqual(findPoisonedBottle(TestCase(444, 1000)), 444)


if __name__ == "__main__":
    unittest.main()
