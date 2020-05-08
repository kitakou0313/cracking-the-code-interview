import unittest


def urlify(s, length):
    s1 = s
    cnt = 0
    for i in range(length):
        if s1[i] == " ":
            cnt += 1

    ind = length + cnt * 2 - 1
    for i in range(length - 1, -1, -1):
        if s1[i] == " ":
            s1[ind] = "0"
            s1[ind - 1] = "2"
            s1[ind - 2] = "%"
            ind -= 3
        else:
            s1[ind] = s1[i]
            ind -= 1
    print(s1)
    return s1


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
