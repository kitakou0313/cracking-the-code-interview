import unittest
import random


class Piece():
    def __init__(self):
        self.connectedPieces = set()
        self.fitPieces = set()

    def setFitPiece(self, other):
        self.fitPieces.add(other)
        other.fitPieces.add(self)

    def connectPiece(self, other):
        self.connectedPieces.add(other)
        other.connectedPieces.add(self)


class Puzzle():
    def __init__(self, N):
        self.N = N
        self.pieces = [[Piece() for i in range(N)] for j in range(N)]

        for i in range(1, N):
            for j in range(1, N):
                self.pieces[i][j].setFitPiece(self.pieces[i-1][j])
                self.pieces[i][j].setFitPiece(self.pieces[i][j-1])

        self.pieces = sum(self.pieces, [])

        for i in range(N):
            j = random.randint(0, N)
            self.pieces[i], self.pieces[j] = self.pieces[j], self.pieces[i]

    def isSolved(self):
        for p in self.pieces:
            if p.fitPieces != p.connectedPieces:
                return False
        return True

    def solve(self):
        for p1 in self.pieces:
            for p2 in self.pieces:
                if p1 in p2.fitPieces:
                    p1.connectPiece(p2)


class Test(unittest.TestCase):
    def test_puzzle(self):
        puzzle = Puzzle(20)
        self.assertEqual(puzzle.isSolved(), False)
        puzzle.solve()
        self.assertEqual(puzzle.isSolved(), True)


if __name__ == "__main__":
    unittest.main()
