import unittest


def reOdrderArrayWithPeakAndValley(array):
    "indx%2 = 0 が山、それ以外が谷とする"
    for ind in range(len(array) - 1):
        if ind % 2 == 0:
            if array[ind] >= array[ind + 1]:
                array[ind], array[ind + 1] = array[ind + 1], array[ind]
        else:
            if array[ind] <= array[ind + 1]:
                array[ind], array[ind + 1] = array[ind + 1], array[ind]


class Test(unittest.TestCase):
    def test_peaks_and_valleys(self):
        a = [12, 6, 3, 1, 0, 14, 13, 20, 22, 10]

        reOdrderArrayWithPeakAndValley(a)

        for i in range(1, len(a)-1):
            self.assertEqual((a[i-1] <= a[i] and a[i] >= a[i + 1])
                             or (a[i-1] >= a[i] and a[i] <= a[i + 1]), True)

        b = [34, 55, 60, 65, 70, 75, 85, 10, 5, 16]

        reOdrderArrayWithPeakAndValley(b)
        for i in range(1, len(a)-1):
            self.assertEqual((a[i-1] <= a[i] and a[i] >= a[i + 1])
                             or (a[i-1] >= a[i] and a[i] <= a[i + 1]), True)


if __name__ == "__main__":
    unittest.main()
