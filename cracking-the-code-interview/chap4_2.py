import unittest


class BSTNode():
    def __init__(self, data, leftNode=None, rightNode=None):
        self.data, self.left, self.right = data, leftNode, rightNode

    def __str__(self):
        string = "(" + str(self.data)
        if self.left:
            string += str(self.left)
        else:
            string += "."

        if self.right:
            string += str(self.right)
        else:
            string += "."

        return string + ")"


def minimalHeightBST(sortedArray):
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0], None, None)
    elif len(sortedArray) == 0:
        return None

    cntInd = len(sortedArray) // 2

    return BSTNode(sortedArray[cntInd], minimalHeightBST(sortedArray[:cntInd]), minimalHeightBST(sortedArray[cntInd + 1:]))


class Test(unittest.TestCase):
    def test_minimal_height_bst(self):
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        bst = minimalHeightBST(sorted_array)
        self.assertEqual(str(bst), "(5(3(2(1..).)(4..))(8(7(6..).)(9..)))")


if __name__ == "__main__":
    unittest.main()
