import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def isSameTree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
        return False

    if tree1.data == tree2.data:
        return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
    else:
        False


def isSubtree(tree1, tree2):
    headOf1 = tree1
    while not(headOf1 is None) and headOf1.data != tree2.data:
        if tree2.data < headOf1.data:
            headOf1 = headOf1.left
        else:
            headOf1 = headOf1.right

    if headOf1 is None:
        return False
    else:
        return isSameTree(headOf1, tree2)


class Test(unittest.TestCase):
    def test_isSubtree(self):
        tree1 = Node(5, Node(3, Node(2), Node(4)),
                     Node(8, Node(7, Node(9)), Node(1)))
        tree2 = Node(8, Node(7), Node(1))
        self.assertEqual(isSubtree(tree1, tree2), False)
        tree3 = Node(8, Node(7, Node(9)), Node(1))
        self.assertEqual(isSubtree(tree1, tree3), True)


if __name__ == "__main__":
    unittest.main()
