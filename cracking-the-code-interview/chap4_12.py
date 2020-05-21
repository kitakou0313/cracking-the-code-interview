import unittest
import random


class Node():
    def __init__(self, name, val, left=None, right=None):
        self.name, self.val, self.left, self.right = name, val, left, right


def getParticalPathNum(node, runningSum, targetSum, wayDic):
    if node is None:
        return 0

    runningSum += node.val
    nowSum = runningSum - targetSum
    totalPaths = wayDic[nowSum] if (nowSum in wayDic) else 0

    if runningSum == targetSum:
        totalPaths += 1

    wayDic[runningSum] = 0
    wayDic[runningSum] += 1

    totalPaths += getParticalPathNum(node.left, runningSum, targetSum, wayDic)
    totalPaths += getParticalPathNum(node.right, runningSum, targetSum, wayDic)

    wayDic[runningSum] -= 1

    return totalPaths


def findPathNumWithSum(node, sum):
    dic = {}
    return getParticalPathNum(node, 0, sum, dic)


class Test(unittest.TestCase):
    def test_paths_with_sum(self):
        bt = Node("A", 4, Node("B", -2, Node("D", 7), Node("E", 4)),
                  Node("C", 7, Node("F", -1, Node("H", -1), Node("I", 2, Node("K", 1))),
                       Node("G", 0, None,        Node("J", -2))))
        self.assertEqual(findPathNumWithSum(bt, 12), 1)
        self.assertEqual(findPathNumWithSum(bt, 2), 4)
        self.assertEqual(findPathNumWithSum(bt, 9), 4)


if __name__ == "__main__":
    unittest.main()
