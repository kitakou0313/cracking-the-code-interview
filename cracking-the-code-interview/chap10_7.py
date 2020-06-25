import unittest
import random


def generateMissingInt(intArray):
    cntNumsOnEachLevel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for num in intArray:
        cntNumsOnEachLevel[num // 1000] += 1

    for level in range(len(cntNumsOnEachLevel)):
        if cntNumsOnEachLevel[level] != 1000:
            existingNum = set([])
            for num in intArray:
                if num >= level*1000 and num < (level + 1)*1000:
                    existingNum.add(num)

            for probMissingNum in range(1000):
                if not(level * 1000 + probMissingNum in existingNum):
                    return level * 1000 + probMissingNum


class Test(unittest.TestCase):
    def test_missing_int(self):
        integer_list = [i for i in range(290)]
        integer_list += [i for i in range(291, 10000)]
        random.shuffle(integer_list)
        integer = generateMissingInt(integer_list)
        self.assertEqual(integer, 290)

        integer_list = [i for i in range(2005)]
        integer_list += [i for i in range(2006, 10000)]
        random.shuffle(integer_list)
        integer = generateMissingInt(integer_list)
        self.assertEqual(integer, 2005)


if __name__ == "__main__":
    unittest.main()
