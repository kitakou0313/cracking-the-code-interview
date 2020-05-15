import unittest


class Stack():
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        if (len(self.list) == 0):
            return None
        val = self.list.pop()

        return val

    def __str__(self):
        string = ""

        for val in self.list.__reversed__():
            string += str(val) + ","

        return string + "None"

    def isEmpty(self):
        return len(self.list) == 0

    def peek(self):
        return self.list[-1] if len(self.list) != 0 else None


def sort_stack(stack):
    tmp = Stack()
    while not(stack.isEmpty()):
        if (tmp.peek() is None):
            tmp.push(stack.pop())
        elif stack.peek() >= tmp.peek():
            tmp.push(stack.pop())
        else:
            tmp2 = Stack()
            while not(tmp.isEmpty() or tmp.peek() <= stack.peek()):
                tmp2.push(tmp.pop())

            tmp.push(stack.pop())

            while not(tmp2.isEmpty()):
                tmp.push(tmp2.pop())

    while not(tmp.isEmpty()):
        stack.push(tmp.pop())

    return stack


class Test(unittest.TestCase):
    def test_sort_stack(self):
        stack = Stack()
        stack.push(10)
        stack.push(30)
        stack.push(70)
        stack.push(40)
        stack.push(80)
        stack.push(20)
        stack.push(90)
        stack.push(50)
        stack.push(60)
        self.assertEqual(str(stack), "60,50,90,20,80,40,70,30,10,None")
        self.assertEqual(str(sort_stack(stack)),
                         "10,20,30,40,50,60,70,80,90,None")


if __name__ == "__main__":
    unittest.main()
