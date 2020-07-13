import unittest


def getMasterMindHitAndBlow(answer, perdict):
    colorAndCntDic = {
        "R": [0, 0], "G": [0, 0], "B": [0, 0], "Y": [0, 0]  # (hit, blow)
    }

    for color in colorAndCntDic:
        for perdictInd in range(len(perdict)):
            if color == perdict[perdictInd]:
                for answerInd in range(len(answer)):
                    if color == answer[answerInd]:
                        if perdictInd == answerInd:
                            colorAndCntDic[color][0] = 1
                        else:
                            colorAndCntDic[color][1] = 1

    ans = [0, 0]
    for color in colorAndCntDic:
        if colorAndCntDic[color][0] != 0:
            ans[0] += colorAndCntDic[color][0]
        else:
            ans[1] += colorAndCntDic[color][1]

    return tuple(ans)


class Test(unittest.TestCase):
    def test_getMasterMindHitAndBlow(self):
        self.assertEqual(getMasterMindHitAndBlow("YYBB", "BBYY"), (0, 2))
        self.assertEqual(getMasterMindHitAndBlow("BYBB", "BBYY"), (1, 1))
        self.assertEqual(getMasterMindHitAndBlow("RGBY", "RGBY"), (4, 0))
        self.assertEqual(getMasterMindHitAndBlow("RGBY", "RBGY"), (2, 2))
        self.assertEqual(getMasterMindHitAndBlow("RGBY", "RRRR"), (1, 0))
        self.assertEqual(getMasterMindHitAndBlow("RRRR", "RBGY"), (1, 0))
        self.assertEqual(getMasterMindHitAndBlow("RRYY", "RYGY"), (2, 0))


if __name__ == "__main__":
    unittest.main()
