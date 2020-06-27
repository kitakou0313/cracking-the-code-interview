import unittest


def searchPosOfNumInSortedMatrix(matrix, trgNum):
    row = 0
    col = len(matrix[0])-1
    # 各行。列ごとの最大、最小値を見て狭めていく

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == trgNum:
            return (row, col)

        if matrix[row][col] < trgNum:
            row += 1
        else:
            col -= 1


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
