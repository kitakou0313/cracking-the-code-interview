import unittest


class Listy(object):
    def __init__(self, array):
        self._array = array

    def __getitem__(self, ix):
        if ix < len(self._array):
            return self._array[ix]
        else:
            return -1


def searchIndWithBinSearchFromListy(listy, targetNum,  left, right):
    mid = (left + right) // 2
    if listy[mid] == targetNum:
        return mid

    if right < left:
        return None

    if targetNum < listy[mid]:
        return searchIndWithBinSearchFromListy(listy, targetNum, left, mid - 1)
    else:
        lengthOfListy = 1
        while listy[mid + 1 + lengthOfListy] != -1:
            lengthOfListy *= 2

        return searchIndWithBinSearchFromListy(listy, targetNum, mid + 1, min(mid + 1 + lengthOfListy, right))


def searchIndOfTargetNumFromListy(listy, targetNum):

    lengthOfListy = 1
    while listy[lengthOfListy - 1] != -1:
        lengthOfListy *= 2

    mid = (lengthOfListy-1) // 2

    if listy[mid] == targetNum:
        return mid

    if targetNum < listy[mid]:
        return searchIndWithBinSearchFromListy(listy, targetNum, 0, mid - 1)
    else:
        if listy[mid + 1] == -1:
            return None
        lengthOfListy = 1
        while listy[mid + 1 + lengthOfListy] != -1:
            lengthOfListy *= 2

        return searchIndWithBinSearchFromListy(listy, targetNum, mid + 1, mid + 1+lengthOfListy)


class Test(unittest.TestCase):
    def test_search_listy(self):
        listy = Listy([1, 7, 11, 22, 33, 44, 55, 66, 77, 88, 99])  # 11
        self.assertEqual(searchIndOfTargetNumFromListy(listy, 25), None)
        self.assertEqual(searchIndOfTargetNumFromListy(listy, 1), 0)
        self.assertEqual(searchIndOfTargetNumFromListy(listy, 22), 3)
        self.assertEqual(searchIndOfTargetNumFromListy(listy, 66), 7)
        self.assertEqual(searchIndOfTargetNumFromListy(listy, 77), 8)
        self.assertEqual(searchIndOfTargetNumFromListy(listy, 99), 10)
        self.assertEqual(searchIndOfTargetNumFromListy(listy, 100), None)

        listy2 = Listy([10, 20, 30, 40, 50, 60, 70, 80])
        self.assertEqual(searchIndOfTargetNumFromListy(listy2, 90), None)
        self.assertEqual(searchIndOfTargetNumFromListy(listy2, 40), 3)


if __name__ == "__main__":
    unittest.main()
