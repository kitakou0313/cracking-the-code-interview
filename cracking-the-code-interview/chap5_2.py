import unittest


def binary_to_string(dnum):
    ans = "0."
    while len(ans) <= 33:
        dnum *= 2
        if dnum >= 1:
            ans += "1"
            dnum -= 1
        else:
            ans += "0"
        if dnum == 0:
            break
    return ans if len(ans) <= 33 else "Insufficient precision"


class Test(unittest.TestCase):
    def test_binary_to_string(self):
        self.assertEqual(binary_to_string(0.75), "0.11")
        self.assertEqual(binary_to_string(0.625), "0.101")
        self.assertEqual(binary_to_string(0.3),
                         "Insufficient precision")


if __name__ == "__main__":
    unittest.main()
