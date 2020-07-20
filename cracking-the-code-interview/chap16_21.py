import unittest


def findPairEqualizingSums(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    sumOfarr1 = sum(arr1)
    sumOfarr2 = sum(arr2)

    diff = sumOfarr1 - sumOfarr2
    if diff % 2 == 1:
        return None

    diff = diff // 2

    indOf2 = 0
    for indOf1 in range(len(arr1)):
        while arr1[indOf1] > (arr2[indOf2] + diff):
            indOf2 += 1
            if indOf2 == len(arr2):
                return None

        if arr1[indOf1] == (arr2[indOf2] + diff):
            return (arr1[indOf1], arr2[indOf2])

    return None


class Test(unittest.TestCase):
    def test_findPairEqualizingSums(self):
        arr1 = [5, 5, 10]
        arr2 = [4, 4, 8]
        swap = findPairEqualizingSums(arr1, arr2)
        self.assertEqual(swap, (10, 8))
        arr1 = [5, 5, 5]
        arr2 = [6, 4, 6]
        swap = findPairEqualizingSums(arr1, arr2)
        self.assertEqual(swap, None)
        arr1 = [5, 5, 14]
        arr2 = [7, 7, 8]
        swap = findPairEqualizingSums(arr1, arr2)
        self.assertEqual(swap, None)
        arr1 = [4, 10, 8]
        arr2 = [5, 5, 14]
        swap = findPairEqualizingSums(arr1, arr2)
        self.assertEqual(swap, (4, 5))


if __name__ == "__main__":
    unittest.main()
