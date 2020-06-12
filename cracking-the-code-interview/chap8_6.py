import unittest


class Tower():
    def __init__(self, name, discs=None):
        self.name = name
        if discs is None:
            self.discs = []
        else:
            self.discs = discs


def moveDisks(numOfDisk, origin, destination, buffer):
    if numOfDisk == 1:
        moveTop(origin, destination)

    else:
        moveDisks(numOfDisk - 1, origin, buffer, destination)
        moveTop(origin, destination)
        moveDisks(numOfDisk - 1, buffer, destination, origin)


def moveTop(origin, destination):
    if len(destination.discs) == 0:
        destination.discs.append(origin.discs.pop())
    elif origin.discs[-1] >= destination.discs[-1]:
        raise Exception("Disc is bigger than disc on top of destination tower")
    else:
        destination.discs.append(origin.discs.pop())


def towers_of_hanoi(tower1, tower2, tower3):
    numOfDisk = len(tower1.discs)

    moveDisks(numOfDisk - 1, tower1, tower2, tower3)

    moveTop(tower1, tower3)

    moveDisks(numOfDisk - 1, tower2, tower3, tower1)


class Test(unittest.TestCase):
    def test_towers_of_hanoi(self):
        tower1 = Tower("Tower1", [2, 1])
        tower2 = Tower("Tower2")
        tower3 = Tower("Tower3")
        towers_of_hanoi(tower1, tower2, tower3)
        self.assertEqual(tower1.discs, [])
        self.assertEqual(tower2.discs, [])
        self.assertEqual(tower3.discs, [2, 1])

        tower1 = Tower("Tower1", [3, 2, 1])
        tower2 = Tower("Tower2")
        tower3 = Tower("Tower3")
        towers_of_hanoi(tower1, tower2, tower3)
        self.assertEqual(tower1.discs, [])
        self.assertEqual(tower2.discs, [])
        self.assertEqual(tower3.discs, [3, 2, 1])

        tower1 = Tower("Tower1", [6, 5, 4, 3, 2, 1])
        tower2 = Tower("Tower2")
        tower3 = Tower("Tower3")
        towers_of_hanoi(tower1, tower2, tower3)
        self.assertEqual(tower1.discs, [])
        self.assertEqual(tower2.discs, [])
        self.assertEqual(tower3.discs, [6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
