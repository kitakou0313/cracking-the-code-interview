import unittest


def calPermutations(string, memoDic):
    ansList = []

    if string in memoDic:
        return memoDic[string]
    if len(string) == 1:
        return [string]

    for ind in range(len(string)):
        ansList += [string[ind] +
                    res for res in calPermutations(string[:ind] + string[ind + 1:], memoDic)]

    memoDic[string] = ansList
    return ansList


class Test(unittest.TestCase):
    def test_permutations(self):
        resList = calPermutations("ABCD", {})
        resList.sort()
        self.assertEqual(resList, ["ABCD", "ABDC", "ACBD", "ACDB",
                                   "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
                                   "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
                                   "DBAC", "DBCA", "DCAB", "DCBA"])


if __name__ == "__main__":
    unittest.main()
