import unittest


def findDuplicateNumbers(intArray):
    bitVector = 0 << 32010
    ansList = []

    for num in intArray:
        numBitVector = 1 << num

        print(numBitVector & bitVector)
        if numBitVector & bitVector != 0:
            ansList.append(num)

        else:
            bitVector = bitVector | numBitVector

    return ansList


class Test(unittest.TestCase):
    def test_find_duplicates(self):
        array = [1, 2, 2, 3, 4, 55, 20000, 20001, 20002, 20003, 17, 18, 19, 20, 22, 23,
                 7,  3, 3, 55, 20002, 20004, 20005, 20006, 16, 18, 22, 24, 25, 26]
        self.assertEqual(sorted(findDuplicateNumbers(array)),
                         sorted([2, 3, 3, 55, 20002, 18, 22]))


if __name__ == "__main__":
    unittest.main()
