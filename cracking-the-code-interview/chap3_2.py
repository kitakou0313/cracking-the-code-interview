import unittest

# 固定版で実装


class MinStack():
    def __init__(self, stackSize):
        self.data = [None for i in range(stackSize)]
        self.size = 0
        self.stackMin = []

    def isTop(self):
        return len(self.data) == self.size

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        ans = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        if ans == self.stackMin[-1]:
            self.stackMin.pop()

        return ans

    def push(self, val):
        self.data[self.size] = val
        self.size += 1

        if len(self.stackMin) == 0 or self.stackMin[-1] > val:
            self.stackMin.append(val)

    def min(self):
        return self.stackMin[-1] if len(self.stackMin) > 0 else None


class Test(unittest.TestCase):
    def test_min_stack(self):
        min_stack = MinStack(10)
        self.assertEqual(min_stack.min(), None)
        min_stack.push(7)
        self.assertEqual(min_stack.min(), 7)
        min_stack.push(6)
        min_stack.push(5)
        self.assertEqual(min_stack.min(), 5)
        min_stack.push(10)
        self.assertEqual(min_stack.min(), 5)
        self.assertEqual(min_stack.pop(), 10)
        self.assertEqual(min_stack.pop(), 5)
        self.assertEqual(min_stack.min(), 6)
        self.assertEqual(min_stack.pop(), 6)
        self.assertEqual(min_stack.pop(), 7)
        self.assertEqual(min_stack.min(), None)


if __name__ == "__main__":
    unittest.main()
