import unittest


def searchRowInSortedMatrix(matrix, trgNum, left, right):
    mid = (left + right) // 2

    if matrix[mid][0] == trgNum or left == right:
        return mid

    if trgNum < matrix[mid][0]:
        return searchRowInSortedMatrix(matrix, trgNum, left, mid - 1)

    else:
        return searchRowInSortedMatrix(matrix, trgNum, mid + 1, right)


def searchColumnInSortedMatrix(matrix, rowNum, trgNum, left, right):
    mid = (left + right) // 2

    if matrix[rowNum][mid] == trgNum:
        return (rowNum, mid)

    if right < left:
        return None

    if trgNum < matrix[rowNum][mid]:
        return searchColumnInSortedMatrix(matrix, rowNum, trgNum, left, mid - 1)

    else:
        return searchColumnInSortedMatrix(matrix, rowNum, trgNum, mid + 1, right)


def searchPosOfNumInSortedMatrix(matrix, trgNum):
    # 行に二分探索、列に二分探索する O(logN + logM)
    # 行の先頭要素で二文探索、サイズが1になるまで
    trgRow = searchRowInSortedMatrix(matrix, trgNum, 0, len(matrix))

    return searchColumnInSortedMatrix(matrix, trgRow, trgNum, 0, len(matrix[0]))


class Test(unittest.TestCase):
    def test_searchPosOfNumInSortedMatrix(self):
        mat = [[1,   2,  3,  4,  5,  6,  7,  8,  9],
               [5,  10, 15, 20, 25, 30, 35, 40, 45],
               [10, 20, 30, 40, 50, 60, 70, 80, 90],
               [13, 23, 33, 43, 53, 63, 73, 83, 93],
               [14, 24, 34, 44, 54, 64, 74, 84, 94],
               [15, 25, 35, 45, 55, 65, 75, 85, 95],
               [16, 26, 36, 46, 56, 66, 77, 88, 99]]
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 10), (1, 1))
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 13), (3, 0))
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 14), (4, 0))
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 16), (6, 0))
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 56), (6, 4))
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 65), (5, 5))
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 74), (4, 6))
        self.assertEqual(searchPosOfNumInSortedMatrix(mat, 99), (6, 8))


if __name__ == "__main__":
    unittest.main()
