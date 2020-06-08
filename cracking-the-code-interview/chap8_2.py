import unittest


class Queue():
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def isEmpty(self):
        return len(self.array) == 0

    def remove(self):
        if not len(self.array):
            return None
        item = self.array[0]
        del self.array[0]
        return item


def path_through_grid(grid):
    q = Queue()
    R = len(grid)
    C = len(grid[0])
    isVisited = set([])

    q.add((0, 0))
    isVisited.add((0, 0))

    gridPaths = [[[] for c in range(C)] for r in range(R)]

    gridPaths[0][0] = ["start"]

    while not(q.isEmpty()):
        now = q.remove()

        for nxtVec in [(0, 1), (1, 0)]:
            nxtPos = (now[0] + nxtVec[0], now[1] + nxtVec[1])
            if nxtPos[0] < R and nxtPos[1] < C and (not (nxtPos in isVisited)) and grid[nxtPos[0]][nxtPos[1]] != 1:
                q.add(nxtPos)
                isVisited.add(nxtPos)

                gridPaths[nxtPos[0]][nxtPos[1]] = gridPaths[now[0]
                                                            ][now[1]] + ["right" if nxtVec == (0, 1) else "down"]

        if now == (R-1, C-1):
            gridPaths[R - 1][C - 1].append("end")
            return gridPaths[R - 1][C - 1]

    return None


class Test(unittest.TestCase):
    def test_path_through_grid(self):
        grid = [[0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 1, 1, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0]]

        print(path_through_grid(grid))
        self.assertEqual(path_through_grid(grid), ["start", "right", "right",
                                                   "right", "down", "down", "right", "right", "right", "down", "end"])
        grid = [[0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0]]
        self.assertEqual(path_through_grid(grid), None)


if __name__ == "__main__":
    unittest.main()
