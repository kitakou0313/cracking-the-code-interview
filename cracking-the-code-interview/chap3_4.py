import unittest

# 固定版で実装


class QueueViaStacks():
    def __init__(self):
        self.stackNewest = []
        self.stackOldest = []

    def add(self, val):
        self.stackNewest.append(val)
        self.stackOldest = []

        for i in self.stackNewest.__reversed__():
            self.stackOldest.append(i)

    def remove(self):
        ans = self.stackOldest.pop() if len(self.stackOldest) != 0 else None
        self.stackNewest = []

        for i in self.stackOldest.__reversed__():
            self.stackNewest.append(i)

        return ans


class Test(unittest.TestCase):
    def test_queue_via_stacks(self):
        queue = QueueViaStacks()
        queue.add(11)
        queue.add(22)
        queue.add(33)
        self.assertEqual(queue.remove(), 11)
        queue.add(44)
        queue.add(55)
        queue.add(66)
        self.assertEqual(queue.remove(), 22)
        self.assertEqual(queue.remove(), 33)
        self.assertEqual(queue.remove(), 44)
        self.assertEqual(queue.remove(), 55)
        queue.add(77)
        self.assertEqual(queue.remove(), 66)
        self.assertEqual(queue.remove(), 77)
        self.assertEqual(queue.remove(), None)


if __name__ == "__main__":
    unittest.main()
