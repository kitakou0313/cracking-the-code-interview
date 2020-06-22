import unittest


def binSearchInShiftedArray(arr, num, left, right):
    mid = (left + right) // 2

    if arr[mid] == num:
        return mid

    if right < left:
        return -1

    if arr[mid] < arr[right]:
        if arr[mid] <= num and num <= arr[right]:
            return binSearchInShiftedArray(arr, num, mid + 1, right)
        else:
            return binSearchInShiftedArray(arr, num, left, mid - 1)
    elif arr[mid] > arr[left]:
        if arr[left] <= num and num <= arr[mid]:
            return binSearchInShiftedArray(arr, num, left, mid-1)
        else:
            return binSearchInShiftedArray(arr, num, mid + 1, right)


def searchIndOfNumFromSortedShiftedArray(arr, num):
    return binSearchInShiftedArray(arr, num, 0, len(arr) - 1)


class Test(unittest.TestCase):
    def test_rotated_search(self):
        array = [55, 60, 65, 70, 75, 80, 85,
                 90, 95, 15, 20, 25, 30, 35, 40, 45]
        self.assertEqual(searchIndOfNumFromSortedShiftedArray(array, 55), 0)
        self.assertEqual(searchIndOfNumFromSortedShiftedArray(array, 60), 1)
        self.assertEqual(searchIndOfNumFromSortedShiftedArray(array, 90), 7)
        self.assertEqual(searchIndOfNumFromSortedShiftedArray(array, 95), 8)
        self.assertEqual(searchIndOfNumFromSortedShiftedArray(array, 15), 9)
        self.assertEqual(searchIndOfNumFromSortedShiftedArray(array, 30), 12)
        self.assertEqual(searchIndOfNumFromSortedShiftedArray(array, 45), 15)


if __name__ == "__main__":
    unittest.main()
