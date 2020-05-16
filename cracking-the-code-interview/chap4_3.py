import unittest


class TreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.depth = None


def makeListsEachDepth(node, lists, depth):
    if node is None:
        return

    if len(lists) == depth:
        lists.append([])

    lists[depth].append(node.data)
    makeListsEachDepth(node.left, lists, depth + 1)
    makeListsEachDepth(node.right, lists, depth + 1)

    return lists


class Test(unittest.TestCase):
    def test_list_of_depths(self):
        node_h = TreeNode('H')
        node_g = TreeNode('G')
        node_f = TreeNode('F')
        node_e = TreeNode('E', node_g)
        node_d = TreeNode('D', node_h)
        node_c = TreeNode('C', None, node_f)
        node_b = TreeNode('B', node_d, node_e)
        node_a = TreeNode('A', node_b, node_c)
        lists = makeListsEachDepth(node_a, [], 0)
        self.assertEqual(str(lists[0]), "['A']")
        self.assertEqual(str(lists[1]), "['B', 'C']")
        self.assertEqual(str(lists[2]), "['D', 'E', 'F']")
        self.assertEqual(str(lists[3]), "['H', 'G']")
        self.assertEqual(len(lists), 4)


if __name__ == "__main__":
    unittest.main()
