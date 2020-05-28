import unittest


def getAntsConflictProbably(vertexNum):
    return 1 - 2*(0.5 ** vertexNum)


class Test(unittest.TestCase):
    def test_getAntsConflictProbably(self):
        self.assertEqual(getAntsConflictProbably(3), 0.75)
        self.assertEqual(getAntsConflictProbably(4), 0.875)


if __name__ == "__main__":
    unittest.main()
