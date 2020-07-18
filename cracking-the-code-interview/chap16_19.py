import unittest

# 幅探or深探でよさそう


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


def measureAllPondSizes(ponds):
    def measureOnePondSize(ponds, startX, startY, isVisited):
        q = Queue()
        H = len(ponds)
        W = len(ponds[0])

        dVecsX = [0, 0, 1, -1, 1, -1, 1, -1]
        dVecsY = [1, -1, 0, 0, 1, 1, -1, -1]

        q.add((startX, startY))
        isVisited.add((startX, startY))

        ansPondSize = 0
        while not(q.isEmpty()):
            nowPos = q.remove()
            ansPondSize += 1

            for dVecInd in range(len(dVecsX)):
                nxtX, nxtY = nowPos[0] + \
                    dVecsX[dVecInd], nowPos[1] + dVecsY[dVecInd]

                if (0 <= nxtX and nxtX < W) and (0 <= nxtY and nxtY < H) and ponds[nxtY][nxtX] == 0:
                    if (nxtX, nxtY) not in isVisited:
                        q.add((nxtX, nxtY))
                        isVisited.add((nxtX, nxtY))

        return ansPondSize

    H = len(ponds)
    W = len(ponds[0])

    isVisited = set([])

    ansSizeList = []

    for y in range(H):
        for x in range(W):
            if ponds[y][x] == 0 and (x, y) not in isVisited:
                ansSizeList.append(measureOnePondSize(ponds, x, y, isVisited))

    return sorted(ansSizeList)


class Test(unittest.TestCase):
    def test_measureAllPondSizes(self):
        terrain = [[0, 0, 1, 2, 3, 1, 1, 1],
                   [1, 1, 1, 2, 2, 2, 0, 1],
                   [1, 0, 1, 1, 2, 1, 1, 2],
                   [0, 1, 0, 1, 3, 1, 2, 3]]
        self.assertEqual(measureAllPondSizes(terrain), [1, 2, 3])
        terrain = [[0, 0, 1, 2, 3, 1, 0, 1, 1],
                   [0, 1, 1, 2, 2, 2, 0, 0, 1],
                   [1, 0, 1, 0, 0, 1, 1, 0, 2],
                   [0, 1, 1, 1, 0, 1, 2, 0, 2],
                   [0, 1, 2, 1, 1, 1, 1, 0, 0]]
        self.assertEqual(measureAllPondSizes(terrain), [3, 6, 7])


if __name__ == "__main__":
    unittest.main()
