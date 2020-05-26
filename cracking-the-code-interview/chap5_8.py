import unittest


def drawLine(screen, width, x1, x2, y):
    startFullByte = x1 // 8
    startOffset = x1 % 8

    if startOffset != 0:
        startFullByte += 1

    endFullByte = x2 // 8
    endOffset = x2 % 8

    if endOffset != 7:
        endFullByte -= 1

    for b in range(startFullByte, endFullByte + 1):
        screen[(width // 8) * y + b] = 0xff

    startMask = (0xff >> startOffset)
    endMask = (0xff << (8 - (endOffset + 1)))

    if x1 // 8 == x2 // 8:
        mask = startMask & endMask
        screen[(width // 8)*y + x1 // 8] |= mask
    else:
        if startOffset != 0:
            screen[(width // 8) * y + (x1 // 8)] |= startMask
        if endOffset != 7:
            screen[(width // 8) * y + (x2 // 8)] |= endMask


class Test(unittest.TestCase):
    def test_drawLine(self):
        screen = [0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]
        drawLine(screen, 64, 20, 42, 1)
        self.assertEqual(
            screen, [0]*8 + [0, 0, 15, 255, 255, 224, 0, 0] + [0]*8)


if __name__ == "__main__":
    unittest.main()
