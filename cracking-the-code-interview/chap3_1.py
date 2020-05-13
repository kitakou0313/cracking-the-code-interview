import unittest

# 固定版で実装


class ThreeStacks():
    def __init__(self):
        self.array = [None for i in range(9)]
        self.size = [0, 0, 0]
        self.buttom = [0, 3, 6]

    def isTop(self, stackNum):
        return self.size[stackNum] >= 3

    def isEmpty(self, stackNum):
        return self.size[stackNum] == 0

    def push(self,  val, stackNum,):
        if self.isTop(stackNum):
            raise Exception("Stack overflow")

        self.array[self.buttom[stackNum] + self.size[stackNum]] = val
        self.size[stackNum] += 1

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return None

        num = self.array[self.buttom[stackNum] + self.size[stackNum] - 1]
        self.array[self.buttom[stackNum] + self.size[stackNum] - 1] = None
        self.size[stackNum] -= 1

        return num


class Test(unittest.TestCase):
    def test_three_stacks(self):
        three_stacks = ThreeStacks()
        three_stacks.push(101, 0)
        three_stacks.push(102, 0)
        three_stacks.push(103, 0)
        three_stacks.push(201, 1)
        self.assertEqual(three_stacks.pop(0), 103)
        self.assertEqual(three_stacks.pop(1), 201)
        self.assertEqual(three_stacks.pop(1), None)
        self.assertEqual(three_stacks.pop(2), None)
        three_stacks.push(301, 2)
        three_stacks.push(302, 2)
        self.assertEqual(three_stacks.pop(2), 302)
        self.assertEqual(three_stacks.pop(2), 301)
        self.assertEqual(three_stacks.pop(2), None)


if __name__ == "__main__":
    unittest.main()
