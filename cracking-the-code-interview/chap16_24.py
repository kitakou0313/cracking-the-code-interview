import unittest


def findPairWithSameSum(arr, sum):
    numbersSet = set([])

    for num in arr:
        numbersSet.add(num)

    ansPairs = set([])
    for num in arr:
        trgNum = (sum-num)
        if trgNum in numbersSet:
            minNum = min(num, trgNum)
            maxNum = max(num, trgNum)

            ansPairs.add((minNum, maxNum))

    return ansPairs


class Test(unittest.TestCase):
    def test_pairs_with_sum(self):
        arr = [2, 3, 4, 11, -4]
        self.assertEqual(findPairWithSameSum(arr, 7), {(3, 4), (-4, 11)})
        arr = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 20, 30, -11]
        self.assertEqual(findPairWithSameSum(arr, 55), {
                         (0, 55), (22, 33), (-11, 66), (11, 44)})


if __name__ == "__main__":
    unittest.main()
