import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.parent = None
        if not(left is None):
            self.left.parent = self
        if not(right is None):
            self.right.parent = self


def getMostLeftNode(node):
    if node is None:
        return None
    n = node
    while not(n.left is None):
        n = n.left

    return n


def successor(node):
    if node.right is None:
        n = node
        pn = node.parent

        while (not(pn is None) and pn.left != n):
            n = pn
            pn = pn.parent
        return pn
    else:
        return getMostLeftNode(node.right)


class Test(unittest.TestCase):
    def test_successor(self):
        self.assertEqual(successor(Node(22, Node(11))), None)
        self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
        self.assertEqual(
            successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
        self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
        self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)


if __name__ == "__main__":
    unittest.main()
