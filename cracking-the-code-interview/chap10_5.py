import unittest


def searchIndOfTargetNumWithBinsearch(arr, targetNum, left, right):
    if(left > right):
        return None

    mid = (left + right) // 2
    offset = 0
    while arr[mid + offset] == "" and arr[mid - offset] == "" and (mid + offset < right and mid - offset > left):
        offset += 1

    if arr[offset + mid] != "":
        mid += offset
    else:
        mid -= offset

    if arr[mid] == targetNum:
        return mid

    if arr[mid] == "":
        return None

    if targetNum < arr[mid]:
        return searchIndOfTargetNumWithBinsearch(arr, targetNum, left, mid - 1)
    else:
        return searchIndOfTargetNumWithBinsearch(arr, targetNum, mid + 1, right)


def searchIndOfTargetNumInSparseArray(arr, targetNum):
    right = len(arr) - 1
    return searchIndOfTargetNumWithBinsearch(arr, targetNum, 0, right)


class Test(unittest.TestCase):
    def test_searchIndOfTargetNumInSparseArray(self):
        array = ["", "", 7, "", "", "", "", "",
                 19, "", "", "", "", 37, 40, "", "", ""]
        self.assertEqual(searchIndOfTargetNumInSparseArray(array, 0), None)
        self.assertEqual(searchIndOfTargetNumInSparseArray(array, 7), 2)
        self.assertEqual(searchIndOfTargetNumInSparseArray(array, 19), 8)
        self.assertEqual(searchIndOfTargetNumInSparseArray(array, 37), 13)
        self.assertEqual(searchIndOfTargetNumInSparseArray(array, 40), 14)
        array = ["", 12, "", 18, "", "", "", "", "",
                 "", "", "", "", "", "", "", "", "", ""]
        self.assertEqual(searchIndOfTargetNumInSparseArray(array, 12), 1)
        self.assertEqual(searchIndOfTargetNumInSparseArray(array, 18), 3)


if __name__ == "__main__":
    unittest.main()
