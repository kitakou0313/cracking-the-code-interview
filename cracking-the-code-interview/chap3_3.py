import unittest

# 固定版で実装


class MultiStack():
    def __init__(self, capacity):
        self.stacks = [[]]
        self.capacity = capacity

    def push(self, val):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self):
        havingStackInd = -1
        while not(havingStackInd == -len(self.stacks) or len(self.stacks[havingStackInd]) != 0):
            havingStackInd -= 1

        return self.stacks[havingStackInd].pop() if len(self.stacks[havingStackInd]) != 0 else None

    def pop_at(self, stackAt):
        return self.stacks[stackAt].pop() if len(self.stacks[stackAt]) != 0 else None


class Test(unittest.TestCase):
    def test_multi_stack(self):
        stack = MultiStack(3)
        stack.push(11)
        stack.push(22)
        stack.push(33)
        stack.push(44)
        stack.push(55)
        stack.push(66)
        stack.push(77)
        stack.push(88)
        self.assertEqual(stack.pop(), 88)
        self.assertEqual(stack.pop_at(1), 66)
        self.assertEqual(stack.pop_at(0), 33)
        self.assertEqual(stack.pop_at(1), 55)
        self.assertEqual(stack.pop_at(1), 44)
        self.assertEqual(stack.pop_at(1), None)
        stack.push(99)
        self.assertEqual(stack.pop(), 99)
        self.assertEqual(stack.pop(), 77)
        self.assertEqual(stack.pop(), 22)
        self.assertEqual(stack.pop(), 11)
        self.assertEqual(stack.pop(), None)


if __name__ == "__main__":
    unittest.main()
