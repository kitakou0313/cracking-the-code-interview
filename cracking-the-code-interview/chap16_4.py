import unittest


def judgeWinnerOfSanmoku(board):
    N = len(board)

    # colmun
    for n in range(N):
        p1KomaNum = 0
        p2KomaNum = 0
        for ni in range(N):
            if board[n][ni] == "o":
                p1KomaNum += 1
            elif board[n][ni] == "x":
                p2KomaNum += 1

        if p1KomaNum == N:
            return 0b10

        if p2KomaNum == N:
            return 0b01

    # low

    for n in range(N):
        p1KomaNum = 0
        p2KomaNum = 0
        for ni in range(N):
            if board[ni][n] == "o":
                p1KomaNum += 1
            elif board[ni][n] == "x":
                p2KomaNum += 1

        if p1KomaNum == N:
            return 0b10

        if p2KomaNum == N:
            return 0b01

    # Naname

    p1KomaNum = 0
    p2KomaNum = 0

    for n in range(N):
        if board[n][n] == "o":
            p1KomaNum += 1
        elif board[n][n] == "x":
            p2KomaNum += 1

    if p1KomaNum == N:
        return 0b10

    if p2KomaNum == N:
        return 0b01

    return 0


class Test(unittest.TestCase):
    def test_judgeWinnerOfSanmoku(self):
        board = [["o", "o", "o"],
                 ["x", "x", " "],
                 [" ", "x", "x"]]
        self.assertEqual(judgeWinnerOfSanmoku(board), 0b10)
        board[0][0] = "x"
        self.assertEqual(judgeWinnerOfSanmoku(board), 0b01)
        board[1][1] = "o"
        self.assertEqual(judgeWinnerOfSanmoku(board), 0b00)
        board = [["o", "o", "o", "x"],
                 ["x", "x", "o", "o"],
                 ["x", " ", "x", "x"],
                 ["o", "x", "o", "x"]]
        self.assertEqual(judgeWinnerOfSanmoku(board), 0b00)
        board[0][3] = "o"
        self.assertEqual(judgeWinnerOfSanmoku(board), 0b10)
        board[0][0] = "x"
        self.assertEqual(judgeWinnerOfSanmoku(board), 0b01)
        board[2][2] = "o"
        self.assertEqual(judgeWinnerOfSanmoku(board), 0b10)


if __name__ == "__main__":
    unittest.main()
