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
        nowPattern = copy.deepcopy(pattern)
        while nowInd < len(string):
            p = nowPattern.pop(0)
            if p == "a":
                if aPattern == string[nowInd:nowInd + aLength]:
                    nowInd += aLength
                    if len(nowPattern) == 0:
                        return True
                else:
                    break
            else:
                if bLength != 0 and bPattern == "":
                    bPattern = string[nowInd:nowInd + bLength]
                    nowInd += bLength
                    if len(nowPattern) == 0:
                        return True
                else:
                    if bPattern == string[nowInd:nowInd + bLength]:
                        nowInd += bLength
                        if len(nowPattern) == 0:
                            return True
                    else:
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
