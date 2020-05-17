import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


# return (bool(is BST), min, max)
def validateTree(node):

    leftTreeRes = validateTree(node.left) if not(
        node.left is None) else (True, float("inf"), -float("inf"))

    rightTreeRes = validateTree(node.right) if not(
        node.right is None) else (True,  float("inf"), -float("inf"))

    if (leftTreeRes[0] and rightTreeRes[0]) and leftTreeRes[2] < node.data and node.data <= rightTreeRes[1]:
        return (True, node.data if node.left is None else leftTreeRes[2], node.data if node.right is None else rightTreeRes[1])
    else:
        return (False, None, None)


class Test(unittest.TestCase):
    def test_validateTree(self):
        self.assertEqual(validateTree(Node(3, Node(1), Node(8)))[0], True)
        tree1 = Node(5, Node(3, Node(1), Node(4)), Node(
            7, Node(6), Node(8, None, Node(9))))
        self.assertEqual(validateTree(tree1)[0], True)
        tree2 = Node(7, Node(3, Node(1), Node(8)), Node(9, Node(8), Node(11)))
        self.assertEqual(validateTree(tree2)[0], False)


if __name__ == "__main__":
    unittest.main()
