import unittest


def mergeSortedArrays(arrA, arrB):
    numBottomInd = 0
    for ind in range(len(arrA)):
        if arrA[ind] is None:
            numBottomInd = ind - 1
            break
    offset = len(arrA) - 1 - numBottomInd

    for ind in range(numBottomInd, -1, -1):
        arrA[ind + offset] = arrA[ind]
        arrA[ind] = None

    indInArrayA = 0 + offset
    indInArrayB = 0

    for ind in range(len(arrA)):
        if indInArrayA < len(arrA) and arrA[indInArrayA] <= arrB[indInArrayB]:
            arrA[ind] = arrA[indInArrayA]
            indInArrayA += 1
        else:
            arrA[ind] = arrB[indInArrayB]
            indInArrayB += 1

        if indInArrayB == len(arrB):
            break


class Test(unittest.TestCase):
    def test_sorted_merge(self):
        a = [33, 44, 55, 66, 88, 99, None, None, None]
        b = [11, 22, 77]
        mergeSortedArrays(a, b)
        self.assertEqual(a, [11, 22, 33, 44, 55, 66, 77, 88, 99])
        a = [11, 22, 55, 66, 88, None, None, None]
        b = [33, 44, 99]
        mergeSortedArrays(a, b)
        self.assertEqual(a, [11, 22, 33, 44, 55, 66, 88, 99])


if __name__ == "__main__":
    unittest.main()
