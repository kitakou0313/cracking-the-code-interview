import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def crossTwoList(list1, list2, preList):
    if len(list1) == 0:
        return [preList + list2]
    elif len(list2) == 0:
        return [preList + list1]

    l1 = list1
    l2 = list2

    ans = [l for l in crossTwoList(l1[1:], l2, preList + [l1[0]])]
    ans += [l for l in crossTwoList(l1, l2[1:], preList + [l2[0]])]

    return ans


def makeSequences(node):

    leftSide = makeSequences(node.left) if not(node.left is None) else [[]]
    rightSide = makeSequences(node.right) if not(node.right is None) else [[]]
    return [[node.data] + l
            for i in leftSide for j in rightSide for l in crossTwoList(i, j, [])]


class Test(unittest.TestCase):
    def test_makeSequences(self):
        self.assertEqual(makeSequences(Node(7, Node(4, Node(5)), Node(9))), [
            [7, 4, 5, 9],
            [7, 4, 9, 5],
            [7, 9, 4, 5]])
        self.assertEqual(makeSequences(Node(7, Node(4, Node(5), Node(6)), Node(9))), [
            [7, 4, 5, 6, 9],
            [7, 4, 5, 9, 6],
            [7, 4, 9, 5, 6],
            [7, 9, 4, 5, 6],
            [7, 4, 6, 5, 9],
            [7, 4, 6, 9, 5],
            [7, 4, 9, 6, 5],
            [7, 9, 4, 6, 5]])


if __name__ == "__main__":
    unittest.main()
