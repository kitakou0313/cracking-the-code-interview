import unittest


def getNthBit(num, i):
    return (num >> i) & 1


def getLongestSequence(num):
    lenDic = {}
    ind = 0
    priods = []
    while num >= (2 ** ind):
        if getNthBit(num, ind) == 0:
            ind += 1
        else:
            sind = ind
            eind = ind
            leng = 0
            while num >= (2 ** ind) and getNthBit(num, ind) == 1:
                ind += 1
                eind += 1
                leng += 1
            lenDic[(sind, eind-1)] = leng
            priods.append((sind, eind-1))

    ansLen = -1
    for i in range(len(priods) - 1):
        if priods[i + 1][0] - priods[i][1] <= 2:
            ansLen = max(ansLen, 1 + lenDic[priods[i + 1]] + lenDic[priods[i]])
        else:
            ansLen = max(ansLen, lenDic[priods[i]] + 1)

    ansLen = max(ansLen, lenDic[priods[len(priods) - 1]] + 1)

    return ansLen


class Test(unittest.TestCase):
    def test_getLongestSequence(self):
        self.assertEqual(getLongestSequence(0b1111100), 6)
        self.assertEqual(getLongestSequence(0b0111111), 7)
        #self.assertEqual(getLongestSequence(-1), 64)
        self.assertEqual(getLongestSequence(0b1011110111001111110), 8)


if __name__ == "__main__":
    unittest.main()
