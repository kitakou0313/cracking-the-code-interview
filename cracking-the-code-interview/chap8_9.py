import unittest


def parens(n):

    if n == 1:
        return set(["()"])

    ansSet = set()
    resList = parens(n-1)
    for res in resList:
        ansSet.add("(" + res + ")")
        ansSet.add(res + "()")
        ansSet.add("()" + res)

    return ansSet


class Test(unittest.TestCase):
    def test_parens1(self):
        self.assertEqual(sorted(list(parens(1))), sorted(["()"]))
        self.assertEqual(sorted(list(parens(2))), sorted(["()()", "(())"]))
        self.assertEqual(sorted(list(parens(3))), sorted(["()()()", "()(())", "(())()", "(()())",
                                                          "((()))"]))


if __name__ == "__main__":
    unittest.main()
