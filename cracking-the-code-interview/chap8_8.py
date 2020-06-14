import unittest


def calPermutations(string, memoDic):

    if string in memoDic:
        return memoDic[string]
    if len(string) == 1:
        return [string]

    ansList = set()

    for ind in range(len(string)):
        for res in calPermutations(string[:ind] + string[ind + 1:], memoDic):
            ansList.add(string[ind] + res)

    memoDic[string] = list(ansList)
    return list(ansList)


class Test(unittest.TestCase):
    def test_permutations(self):
        res = calPermutations("ABCD", {})
        res.sort()
        self.assertEqual(res, ["ABCD", "ABDC", "ACBD", "ACDB",
                               "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
                               "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
                               "DBAC", "DBCA", "DCAB", "DCBA"])
        res = calPermutations("abca", {})
        res.sort()
        self.assertEqual(res, ["aabc", "aacb", "abac", "abca",
                               "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])


if __name__ == "__main__":
    unittest.main()
