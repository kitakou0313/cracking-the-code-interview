import unittest


def pal_perm(s):
    s = s.lower()
    s = s.replace(" ", "")

    countOdd = 0

    table = [0 for _ in range(26)]

    for c in s:
        val = ord(c) - ord("a")
        table[val] += 1
        if table[val] % 2 == 1:
            countOdd += 1
        else:
            countOdd -= 1
    return countOdd <= 1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
