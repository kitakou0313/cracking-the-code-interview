import unittest


class Node():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def isBalanced(node):
    if node == None:
        return (True, 0)

    leftResult = isBalanced(node.left)
    rightResult = isBalanced(node.right)

    if (leftResult[0] == True and rightResult[0] == True) and (abs(leftResult[1] - rightResult[1]) <= 1):
        return (True, max(leftResult[1], rightResult[1]) + 1)

    else:
        return (False, None)


class Test(unittest.TestCase):
    def test_isBalanced(self):
        self.assertEqual(isBalanced(Node(Node(), Node())), (True, 2))
        self.assertEqual(isBalanced(Node(Node(), Node(Node()))), (True, 3))
        self.assertEqual(isBalanced(Node(Node(), Node(Node(Node())))),
                         (False, None))
        self.assertEqual(isBalanced(Node(Node(Node()), Node(Node(Node())))),
                         (False, None))
        self.assertEqual(isBalanced(Node(Node(Node()),
                                         Node(Node(Node()), Node()))), (True, 4))


if __name__ == "__main__":
    unittest.main()
