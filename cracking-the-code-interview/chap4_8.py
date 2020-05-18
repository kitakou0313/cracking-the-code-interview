import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def findNode(root, node):
    if root is None:
        return None
    if root == node:
        return root
    return findNode(root.left, node) or findNode(root.right, node)


def getWitchChildHaving(root, node1, node2):
    foundChild = []
    resNode1 = findNode(root, node1)
    resNode2 = findNode(root, node2)
    if not(resNode1 is None):
        foundChild.append(resNode1)
    if not(resNode2 is None):
        foundChild.append(resNode2)
    return foundChild


def getFirstCommonAncestor(treeRoot, node1, node2):

    leftRes = getWitchChildHaving(treeRoot.left, node1, node2)
    rightRes = getWitchChildHaving(treeRoot.right, node1, node2)

    if len(leftRes) == 1 and len(rightRes) == 1 and leftRes[0] in [node1, node2] and rightRes[0] in [node1, node2]:
        return treeRoot
    elif len(leftRes) == 2:
        return getFirstCommonAncestor(treeRoot.left, node1, node2)
    elif len(rightRes) == 2:
        return getFirstCommonAncestor(treeRoot.right, node1, node2)
    else:
        return None


class Test(unittest.TestCase):
    def test_getFirstCommonAncestor(self):
        node1 = Node(11, Node(55), Node(77, Node(44)))
        node2 = Node(22, Node(99))
        self.assertEqual(getFirstCommonAncestor(Node(100), node1, node2), None)
        node3 = Node(33, node1, Node(88, Node(123, None, node2)))
        node4 = Node(44, node3, Node(66))
        self.assertEqual(getFirstCommonAncestor(node4, node1, node2), node3)


if __name__ == "__main__":
    unittest.main()
