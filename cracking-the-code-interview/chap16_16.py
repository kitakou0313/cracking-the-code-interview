import unittest


def findArrayIndsNeededToBeSorted(array):
    startInd, endInd = 0, 0

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            startInd = i
            break

    for i in range(len(array)-1, 0, -1):
        if array[i - 1] > array[i]:
            endInd = i
            break

    return (startInd, endInd)


class Test(unittest.TestCase):
    def test_findArrayIndsNeededToBeSorted(self):
        array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(findArrayIndsNeededToBeSorted(array), (0, 0))
        array = [10, 11, 12, 13, 14, 16, 15, 17, 18, 19]
        self.assertEqual(findArrayIndsNeededToBeSorted(array), (5, 6))
        array = [10, 18, 12, 13, 14, 16, 15, 17, 11, 19]
        self.assertEqual(findArrayIndsNeededToBeSorted(array), (1, 8))
        array = [90, 80, 70, 60, 50, 40, 30, 20, 10, 1]
        self.assertEqual(findArrayIndsNeededToBeSorted(array), (0, 9))


if __name__ == "__main__":
    unittest.main()
