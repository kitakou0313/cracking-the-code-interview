import unittest

"""
草生えないのの検証
"""


class Box(object):
    def __init__(self, height, width, depth):
        self.height, self.width, self.depth = height, width, depth

    def isEnablePuttedOnThisBox(self, box):
        return self.height > box.height and self.width > box.width and self.depth > box.depth


def calMaxHeightWithBox(bottomBox, boxes, memo):
    if bottomBox in memo:
        return memo[bottomBox]

    res = bottomBox.height

    for probNxtbox in boxes:
        if bottomBox.isEnablePuttedOnThisBox(probNxtbox):
            res = max(res, bottomBox.height +
                      calMaxHeightWithBox(probNxtbox, boxes, memo))

    memo[bottomBox] = res
    return res


def calMostHighestBoxStack(boxes):
    maxHeight = -1
    memo = {}

    for box in boxes:
        maxHeight = max(maxHeight, calMaxHeightWithBox(box, boxes, memo))

    return maxHeight


class Test(unittest.TestCase):
    def test_stack_boxes(self):
        boxes = [Box(100, 100, 100)]
        self.assertEqual(calMostHighestBoxStack(boxes), 100)
        boxes.append(Box(25, 25, 25))
        self.assertEqual(calMostHighestBoxStack(boxes), 125)
        boxes.append(Box(20, 5, 30))
        boxes.append(Box(17, 4, 28))
        self.assertEqual(calMostHighestBoxStack(boxes), 137)


if __name__ == "__main__":
    unittest.main()
