import unittest


def findSmallestDiff(a1, a2):
    arr1 = sorted(a1)
    arr2 = sorted(a2)

    ans = float("inf")

    indInArr2 = 0
    for i in range(len(arr1)):
        while indInArr2 < len(arr2) - 1 and abs(arr2[indInArr2] - arr1[i]) >= abs(arr2[indInArr2 + 1] - arr1[i]):
            indInArr2 += 1
        ans = min(ans, abs(arr2[indInArr2] - arr1[i]))

    return ans


class Test(unittest.TestCase):
    def test_findSmallestDiff(self):
        self.assertEqual(findSmallestDiff(
            [11, 22, 33, 44], [77, 2, 66, 50]), 6)
        self.assertEqual(findSmallestDiff(
            [11, 22, 33, 44], [77, 2, 34, 50]), 1)
        self.assertEqual(findSmallestDiff(
            [11, 77, 33, 44], [77, 2, 34, 50]), 0)
        array1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        array2 = [33, 45, 58, 17]
        self.assertEqual(findSmallestDiff(array1, array2), 2)
        self.assertEqual(findSmallestDiff(array2, array1), 2)


if __name__ == "__main__":
    unittest.main()
