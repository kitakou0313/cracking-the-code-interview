import unittest
import copy


def groupAnagrams(strings):
    ansList = []
    addedSet = set([])

    for string in strings:
        if string in addedSet:
            continue

        ansList.append(string)
        addedSet.add(string)
        for posString in strings:
            if not(posString in addedSet) and sorted(string) == sorted(posString):
                ansList.append(posString)
                addedSet.add(posString)

    return ansList


class Test(unittest.TestCase):
    def test_group_anagrams(self):
        strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]

        self.assertEqual(groupAnagrams(sorted(strings)),
                         ['arts', 'star', 'bat', 'tab', 'car', 'cat', 'rat', 'tar'])


if __name__ == "__main__":
    unittest.main()
