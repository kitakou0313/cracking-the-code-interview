import unittest
import copy
# 各左端に区間の和を計算していき、合計が負になったらその左端の探索を打ち切る その区間を含まない方が大きい値になるため
#


def findSectionWithMaxSum(array):
    class SectioWithSum():
        def __init__(self, l, r, Sum):
            self.left, self.right, self.sum = l, r, Sum

    ansSection = SectioWithSum(0, 0, -float("inf"))

    left = 0
    while left < len(array):
        sumFromLeft = 0
        maxSectionWithSum = SectioWithSum(left, left, -float("inf"))

        for right in range(left, len(array)):
            sumFromLeft += array[right]

            if sumFromLeft > maxSectionWithSum.sum:
                maxSectionWithSum.right = right
                maxSectionWithSum.sum = sumFromLeft

            if sumFromLeft < 0:
                break

        ansSection = copy.deepcopy(
            maxSectionWithSum) if maxSectionWithSum.sum > ansSection.sum else ansSection

        left = right + 1

    return (ansSection.left, ansSection.right)


class Test(unittest.TestCase):
    def test_findSectionWithMaxSum(self):
        seq = [-1, 4, 4, -7, 8, 2, -4, 3]
        self.assertEqual(findSectionWithMaxSum(seq), (1, 5))
        seq = [-1, 4, 4, -7, 8, 2, -4, -3, 9]
        self.assertEqual(findSectionWithMaxSum(seq), (1, 8))
        seq = [-1, -4, -54, -7, -8, 2, -4, -3, 9]
        self.assertEqual(findSectionWithMaxSum(seq), (8, 8))
        seq = [-1, -4, -54, -7, -8, -2, -4, -3, -9]
        self.assertEqual(findSectionWithMaxSum(seq), (0, 0))


if __name__ == "__main__":
    unittest.main()
