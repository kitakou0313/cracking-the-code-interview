import unittest


def string_compression(s):
    ans = []
    cnt = 0
    for i in range(len(s)):
        cnt += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            ans.append(s[i] + str(cnt))
            cnt = 0

    return "".join(ans) if len(ans) < len(s) else s


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
