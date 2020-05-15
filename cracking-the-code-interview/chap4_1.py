import unittest


class Queue():
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def isEmpty(self):
        return len(self.array) == 0

    def remove(self):
        if not len(self.array):
            return None
        item = self.array[0]
        del self.array[0]
        return item


class Node():
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.connectedList = adjacency_list or []
        self.shortest_path = None

    def add_edge_to(self, node):
        self.connectedList += [node]

    def __str__(self):
        return self.data


def findRoute(nodeStart, nodeEnd):
    q = Queue()
    isVisited = set([])

    q.add(nodeStart)
    isVisited.add(nodeStart.data)

    ansPath = ""
    isFound = False
    while not(q.isEmpty()):
        node = q.remove()

        for nxtNode in node.connectedList:
            if not (nxtNode.data in isVisited):
                q.add(nxtNode)
                isVisited.add(nxtNode.data)

        ansPath += str(node.data)
        if node == nodeEnd:
            isFound = True
            break

    return str(isFound)


def str_for(path):
    if not path:
        return str(path)
    return ''.join([str(n) for n in path])


class Test(unittest.TestCase):
    def test_find_route(self):
        node_j = Node('J')
        node_i = Node('I')
        node_h = Node('H')
        node_d = Node('D')
        node_f = Node('F', [node_i])
        node_b = Node('B', [node_j])
        node_g = Node('G', [node_d, node_h])
        node_c = Node('C', [node_g])
        node_a = Node('A', [node_b, node_c, node_d])
        node_e = Node('E', [node_f, node_a])
        node_d.add_edge_to(node_a)
        self.assertEqual(str_for(findRoute(node_a, node_i)), "False")
        self.assertEqual(str_for(findRoute(node_a, node_j)), "True")
        node_h.add_edge_to(node_i)
        self.assertEqual(str_for(findRoute(node_a, node_i)), "True")


if __name__ == "__main__":
    unittest.main()
