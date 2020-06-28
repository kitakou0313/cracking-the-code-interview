import unittest


class RankNode():
    def __init__(self, num):
        self._num = num

        self._leftNode, self._rightNode = None, None

        self._leftNodeNum = 0

    def getRankOfNum(self, num, sumRank=0):
        if self._num == num:
            return sumRank + self._leftNodeNum
        else:
            if num < self._num:
                return self._leftNode.getRankOfNum(num, sumRank)
            else:
                return self._rightNode.getRankOfNum(num, sumRank=sumRank + self._leftNodeNum + 1)

    def track(self, num):
        if num <= self._num:
            self._leftNodeNum += 1
            if num == self._num:
                return
            else:
                if self._leftNode is None:
                    self._leftNode = RankNode(num)
                else:
                    self._leftNode.track(num)

        else:
            if self._rightNode is None:
                self._rightNode = RankNode(num)
            else:
                self._rightNode.track(num)


class Test(unittest.TestCase):
    def test_rank_tree(self):
        rt = RankNode(11)
        self.assertEqual(rt.getRankOfNum(11), 0)
        rt.track(30)
        self.assertEqual(rt.getRankOfNum(30), 1)
        rt.track(7)
        rt.track(7)
        rt.track(10)
        rt.track(15)
        rt.track(7)
        rt.track(3)
        rt.track(22)
        self.assertEqual(rt.getRankOfNum(10), 4)
        self.assertEqual(rt.getRankOfNum(3), 0)
        self.assertEqual(rt.getRankOfNum(22), 7)
        self.assertEqual(rt.getRankOfNum(30), 8)


if __name__ == "__main__":
    unittest.main()
