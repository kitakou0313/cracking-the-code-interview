import unittest


class Box(object):
    def __init__(self, height, width, depth):
        self.height, self.width, self.depth = height, width, depth

    def isEnablePuttedOnThisBox(self, box):
        return self.height > box.height and self.width > box.width and self.depth > box.depth


def calMaxHeightWithBox(box, boxes, memo):
    if box in memo:
        return memo[box]

    res = box.height

    for probNxtbox in boxes:
        if box.isEnablePuttedOnThisBox(probNxtbox):
            res = max(res, box.height +
                      calMaxHeightWithBox(probNxtbox, boxes, memo))

    memo[box] = res
    return res


def calHeightMostHighestBosStack(boxes):
    maxHeight = -1
    memo = {}
    boxes.sort(key=lambda b: b.height, reverse=True)
    for box in boxes:
        maxHeight = max(maxHeight, calMaxHeightWithBox(box, boxes, memo))

    return maxHeight


class Test(unittest.TestCase):
    def test_stack_boxes(self):
        boxes = [Box(100, 100, 100)]
        self.assertEqual(calHeightMostHighestBosStack(boxes), 100)
        boxes.append(Box(25, 25, 25))
        self.assertEqual(calHeightMostHighestBosStack(boxes), 125)
        boxes.append(Box(20, 5, 30))
        boxes.append(Box(17, 4, 28))
        self.assertEqual(calHeightMostHighestBosStack(boxes), 137)


if __name__ == "__main__":
    unittest.main()
