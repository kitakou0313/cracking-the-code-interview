import unittest


def insertion(N, M, i, j):
    shiftedM = M << i
    clearedN = N & ~((1 << (j + 1)) - (1 << i))

    return clearedN | shiftedM


class Test(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(insertion(0b11111111, 0b10, 2, 5), 0b11001011)
        self.assertEqual(insertion(0b00000000, 0b1010, 4, 7), 0b10100000)


if __name__ == "__main__":
    unittest.main()
