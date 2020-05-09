import unittest


def zero_matrix(m):

    if len(m) == 0 or len(m[0]) == 0:
        return False

    to0Rows = []
    to0Col = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                to0Col.append(j)
                to0Rows.append(i)

    for i in to0Rows:
        for j in range(len(m[0])):
            m[i][j] = 0

    for i in to0Col:
        for j in range(len(m)):
            m[j][i] = 0

    return m


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
