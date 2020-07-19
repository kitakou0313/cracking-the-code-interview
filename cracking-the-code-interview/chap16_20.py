import unittest


def decodeDigitsToWords(digits):
    LETTERS = {0: [], 1: [], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    WORDS = ["tree", "used", "abacus", "unko", "test", "end"]

    def makeDicDigitsWithWords(WORDS):
        digitsAndWord = {}
        for word in WORDS:
            digits = ""
            for char in word:
                for digit in LETTERS:
                    if char in LETTERS[digit]:
                        digits += str(digit)

            if digits not in digitsAndWord:
                digitsAndWord[digits] = [word]
            else:
                digitsAndWord[digits].append(word)
        return digitsAndWord

    dic = makeDicDigitsWithWords(WORDS)

    return dic[digits]


class Test(unittest.TestCase):
    def test_decodeDigitsToWords(self):
        digits = "222287"
        self.assertEqual(decodeDigitsToWords(digits), ['abacus'])
        digits = "8733"
        self.assertEqual(decodeDigitsToWords(digits), ['tree', 'used'])


if __name__ == "__main__":
    unittest.main()
