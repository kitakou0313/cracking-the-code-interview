import unittest
import random


class Node():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.size = 1  # 自分を根とする木のノード数
        self.size += left.size if not left is None else 0
        self.size += right.size if not right is None else 0

    def get_random_node(self):
        index = random.randint(1, self.size)
        if index == self.size:
            return self
        elif index <= self.left.size:
            return self.left.get_random_node()
        else:
            return self.right.get_random_node()

    def insert(self, data):
        current = self
        while True:
            current.size += 1
            if current.left is None and current.right is None:
                index = random.randint(1, 2)
                if index == 1:
                    current.left = Node(data)
                else:
                    current.right = Node(data)
                break
            elif current.left is None:
                current.left = Node(data)
                break
            elif current.right is None:
                current.right = Node(data)
                break

            index = random.randint(1, 2)
            if index == 1:
                current = current.left
            else:
                current = current.right


tree = Node(11)
tree.insert(21)
tree.insert(44)
tree.insert(31)

resList = []

for i in range(100000):
    resList.append(tree.get_random_node().data)

ansDic = {11: 0, 21: 0, 31: 0, 44: 0}

for res in resList:
    ansDic[res] += 1

print(ansDic)
