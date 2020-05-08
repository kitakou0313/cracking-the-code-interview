import unittest


def isOrdered(s1, s2):
    if len(s1) != len(s2):
        return False

    charSet = [0 for _ in range(128)]
    for c in s1:
        val = ord(c)
        charSet[val] += 1
    for c in s2:
        val = ord(c)
        charSet[val] -= 1
        if charSet[val] < 0:
            return False

    return True if sum(charSet) == 0 else False


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = isOrdered(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = isOrdered(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
