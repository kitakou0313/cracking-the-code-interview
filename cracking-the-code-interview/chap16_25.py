import unittest
from LinkedList import LinkedListNode

"""
head            tail
prev => node => next
New             old
"""


class DoubleLinkedListForLRU():
    def __init__(self, maxCapacity):
        self.head = self.tail = None
        self.size = 0
        self.maxCapacity = maxCapacity

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def deleteTailNode(self):
        deletedKey = self.tail.value

        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1

        return deletedKey

    def addNodeToHead(self, node):
        if self.head is None:
            self.head = self.tail = node
            self.size += 1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.size += 1

        if self.size == self.maxCapacity + 1:
            return self.deleteTailNode()

    def moveNodeToHead(self, node):
        if node == self.head:
            return
        else:
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev

            node.next = self.head
            node.prev = None

            self.head = node


class Record():
    def __init__(self, value, node):
        self.value, self.node = value, node


class LRUCache():

    def __init__(self, cacheSize=0):
        # 参照記録保持用 headが最新, tailが最古 なので一番後ろから消してけば良い
        self.keyList = DoubleLinkedListForLRU(cacheSize)

        #keyからvalue, 及びnodeへの参照をもつ
        self.valueList = {}

    def add(self, key, value):
        keyNode = LinkedListNode(key)
        self.valueList[key] = Record(value, keyNode)
        addingRes = self.keyList.addNodeToHead(keyNode)

        if addingRes != None:
            del self.valueList[addingRes]

    def lookup(self, key):
        if key in self.valueList:
            self.keyList.moveNodeToHead(self.valueList[key].node)
            return self.valueList[key].value
        else:
            return None

    def ages(self):
        resList = []
        ind = 0
        for node in self.keyList:
            resList.append((node.value, ind))
            ind += 1
        return resList


class Test(unittest.TestCase):
    def test_lru_cache(self):
        cache = LRUCache(4)
        cache.add('food',  'lasagna')
        cache.add('drink', 'orange juice')
        cache.add('color', 'green')
        cache.add('dance', 'bachata')
        self.assertEqual(sorted(cache.ages()),
                         sorted([('food', 3), ('drink', 2), ('color', 1), ('dance', 0)]))
        #[('food', 0), ('drink', 1), ('color', 2), ('dance', 3)]
        cache.add('sport', 'ultimate')
        self.assertEqual(sorted(cache.ages()),
                         sorted([('drink', 3), ('dance', 1),
                                 ('color', 2), ('sport', 0)]))
        #[('drink', 1), ('dance', 3), ('color', 2), ('sport', 4)]
        self.assertEqual(cache.lookup('dance'), 'bachata')
        self.assertEqual(sorted(cache.ages()),
                         sorted([('drink', 3), ('sport', 1),
                                 ('color', 2), ('dance', 0)]))
        #[('drink', 1), ('sport', 4),('color', 2), ('dance', 5)]
        self.assertEqual(cache.lookup('food'), None)
        cache.add('spice', 'paprika')
        self.assertEqual(sorted(cache.ages()),
                         sorted([('color', 3), ('sport', 2),
                                 ('spice', 0), ('dance', 1)]))
        self.assertEqual(cache.lookup('drink'), None)
        self.assertEqual(cache.lookup('color'), 'green')
        self.assertEqual(cache.lookup('color'), 'green')
        self.assertEqual(sorted(cache.ages()),
                         sorted([('sport', 3), ('dance', 2),
                                 ('spice', 1), ('color', 0)]))


if __name__ == "__main__":
    unittest.main()
