import unittest


def findMagicIndWithBinS(l, start, end):
    mid = (start + end) // 2

    if start > mid:
        return None

    if l[mid] < mid:
        return findMagicIndWithBinS(l, mid + 1, end)
    elif l[mid] > mid:
        return findMagicIndWithBinS(l, start, mid - 1)
    elif l[mid] == mid:
        return mid


def magic_index_distinct(l):
    return findMagicIndWithBinS(l, 0, len(l) - 1)


def findMagicIndWithBinSFromUndistinct(l, start, end):
    mid = (start + end) // 2
    if start > mid:
        return None
    midValue = l[mid]

    if mid == midValue:
        return mid

    leftRes = findMagicIndWithBinSFromUndistinct(
        l, max(mid + 1, midValue), end)
    if leftRes is not None:
        return leftRes

    rightRes = findMagicIndWithBinSFromUndistinct(
        l, start, min(mid - 1, midValue))

    if rightRes is not None:
        return rightRes

    return None


def magic_index(l):
    return findMagicIndWithBinSFromUndistinct(l, 0, len(l) - 1)


class Test(unittest.TestCase):
    def test_magic_index_distinct(self):
        self.assertEqual(magic_index_distinct([3, 4, 5]), None)
        self.assertEqual(magic_index_distinct([-2, -1, 0, 2]), None)
        self.assertEqual(magic_index_distinct(
            [-20, 0, 1, 2, 3, 4, 5, 6, 20]), None)
        self.assertEqual(magic_index_distinct(
            [-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index_distinct([-20, 1, 2, 3, 4, 5, 6, 20]), 3)

    def test_magic_index(self):
        self.assertEqual(magic_index([3, 4, 5]), None)
        self.assertEqual(magic_index([-2, -1, 0, 2]), None)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 6, 20]), None)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index([-20, 5, 5, 5, 5, 5, 7, 20]), 5)


if __name__ == "__main__":
    unittest.main()
