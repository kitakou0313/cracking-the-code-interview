import unittest


def findArrayIndsNeededToBeSorted(array):
    def findMiddleArray(array):
        startInd, endInd = 0, 0

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                startInd = i
                break

        for i in range(len(array)-1, 0, -1):
            if array[i - 1] > array[i]:
                endInd = i
                break
        return startInd, endInd

    startInd, endInd = findMiddleArray(array)

    if startInd == 0 and endInd == 0:
        return(0, 0)

    middleArrMin = array[startInd]
    middleArrMax = array[startInd]

    for i in range(startInd, endInd+1):
        middleArrMax = max(middleArrMax, array[i])
        middleArrMin = min(middleArrMin, array[i])

    ansStartInd = startInd
    ansEndInd = endInd

    for i in range(startInd-1, -1, -1):
        if array[i] > middleArrMin:
            ansStartInd = i

    for i in range(endInd+1, len(array)):
        if array[i] < middleArrMax:
            ansEndInd = i

    return (ansStartInd, ansEndInd)


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

        array = [1, 2, 4, 7, 10, 11, 8, 12, 5, 6, 16, 18, 19]
        #                        koko       koko
        self.assertEqual(findArrayIndsNeededToBeSorted(array), (3, 9))


if __name__ == "__main__":
    unittest.main()
