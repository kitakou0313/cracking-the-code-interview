import unittest
import copy


def findMatchingPatterns(string, pattern):
    def normalizePattern(pattern):
        if pattern[0] == "a":
            return pattern
        else:
            normalizedP = ""
            for p in pattern:
                normalizedP += "a" if p == "b" else "b"
            return normalizedP

    pattern = list(normalizePattern(pattern))

    aCount = 0
    bCount = 0
    for p in pattern:
        if p == "a":
            aCount += 1
        else:
            bCount += 1

    for aLength in range(1, len(string) // aCount + 1):
        bLength = (len(string) - aCount *
                   aLength)//bCount if bCount != 0 else 0
        aPattern = string[:aLength]
        bPattern = ""

        nowInd = 0

        for p in range(len(pattern)):
            if pattern[p] == "a":
                if string[nowInd:nowInd + aLength] == aPattern:
                    nowInd += aLength
                else:
                    break

            elif pattern[p] == "b":
                if bLength != 0 and bPattern == "":
                    bPattern = string[nowInd:nowInd + bLength]
                    nowInd += bLength
                    continue
                if string[nowInd:nowInd + bLength] == bPattern:
                    nowInd += bLength
                else:
                    break

            if p == len(pattern) - 1:
                return True

            if nowInd >= len(string):
                break

    return False


class Test(unittest.TestCase):
    def test_findMatchingPatterns(self):
        self.assertTrue(findMatchingPatterns("dogdogturtledog", "aaba"))
        self.assertTrue(findMatchingPatterns("dogdogturtledog", "bbab"))
        self.assertTrue(findMatchingPatterns("dogdogturtledogdog", "aabaa"))
        self.assertTrue(findMatchingPatterns("dogdogturtledogdog", "aba"))
        self.assertTrue(findMatchingPatterns("dogdogturtledogdo", "aba"))
        self.assertFalse(findMatchingPatterns("dogdogturtledogdg", "aba"))
        self.assertTrue(findMatchingPatterns("catcatbirdbird", "aabb"))
        self.assertFalse(findMatchingPatterns("catcatcatbirdbird", "aabb"))
        self.assertTrue(findMatchingPatterns(
            "buffalobuffalobuffalobuffalo", "aaaa"))
        self.assertFalse(findMatchingPatterns(
            "buffalobuffalouffalobuffalo", "aaaa"))


if __name__ == "__main__":
    unittest.main()
