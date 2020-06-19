import unittest


def countValidBracketsPos(string, wishBool):
    if len(string) == 1:
        if (string == "1" and wishBool == True) or (string == "0" and wishBool == False):
            return 1
        else:
            return 0

    ans = 0

    boolDic = {
        "&": {True: [(True, True)], False: [(True, False), (False, True), (False, False)]},
        "|": {True: [(True, False), (False, True), (True, True)], False: [(False, False)]},
        "^": {True: [(True, False), (False, True)], False: [(False, False), (True, True)]}
    }

    for ind in range(len(string)):
        if string[ind] != "0" and string[ind] != "1":
            leftString = string[:ind]
            rightString = string[ind + 1:]
            for validBoolPair in boolDic[string[ind]][wishBool]:
                ans += countValidBracketsPos(leftString, validBoolPair[0]) * countValidBracketsPos(
                    rightString, validBoolPair[1])

    return ans


class Test(unittest.TestCase):
    def test_countValidBracketsPos(self):
        self.assertEqual(countValidBracketsPos("1", True), 1)
        self.assertEqual(countValidBracketsPos("0", True), 0)
        self.assertEqual(countValidBracketsPos("0", False), 1)
        self.assertEqual(countValidBracketsPos("1&1", True), 1)
        self.assertEqual(countValidBracketsPos("1|0", False), 0)
        self.assertEqual(countValidBracketsPos("1^0", True), 1)
        self.assertEqual(countValidBracketsPos("1&0&1", True), 0)
        self.assertEqual(countValidBracketsPos("1|1^0", True), 2)
        self.assertEqual(countValidBracketsPos("1^0|0|1", False), 2)
        self.assertEqual(countValidBracketsPos("1^0|0|1", True), 3)
        self.assertEqual(countValidBracketsPos("0&0&0&1^1|0", True), 10)


if __name__ == "__main__":
    unittest.main()
