import unittest


def power_set(sets):
    N = len(sets)
    factors = []
    ansSets = set()

    for i in range(N):
        factors.append(sets.pop())

    factors.sort()

    for i in range(2 ** N):
        tagNum = i
        subSets = set()

        ind = 0
        while tagNum != 0:
            if tagNum & 1 == 1:
                subSets.add(factors[ind])
            tagNum >>= 1
            ind += 1

        ansSets.add(frozenset(subSets))

    return ansSets


class Test(unittest.TestCase):
    def test_power_set(self):
        s = {'a', 'b', 'c', 'd'}
        ps = power_set(s)
        self.assertEqual(len(ps), 16)
        subsets = [set(), {'a'}, {'b'}, {'c'}, {'d'},
                   {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {
            'b', 'c'}, {'b', 'd'}, {'c', 'd'},
            {'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'}, s]

        for subset in subsets:
            self.assertEqual(subset in ps, True)

        #self.assertEqual(ps, set([frozenset(s) for s in subsets]))


if __name__ == "__main__":
    unittest.main()
