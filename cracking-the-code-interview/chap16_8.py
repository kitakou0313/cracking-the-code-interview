import unittest

SINGLE_DIGITS = {0: "zero", 1: "one", 2: "two", 3: "three",
                 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

FROM_10_TO_19 = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

FROM_20_TO_90 = {20: "twenty", 30: "thirty", 40: "forty",
                 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def transrateBitween0To99(number):
    if 0 <= number and number <= 9:
        return SINGLE_DIGITS[number]
    elif 10 <= number and number <= 19:
        return FROM_10_TO_19[number]
    elif 20 <= number and number <= 99:
        return FROM_20_TO_90[(number // 10)*10] + ((" " + SINGLE_DIGITS[number % 10]) if number % 10 != 0 else "")


def transrateBitween0To999(number):
    if 0 <= number and number <= 99:
        return transrateBitween0To99(number)
    else:  # 100 ~ 999
        return SINGLE_DIGITS[(number // 100)] + " hundred" + ("" if number % 100 == 0 else (" " + transrateBitween0To99(number % 100)))


def transrateOver1000(number):
    levelInd = 0
    levels = ["thousand", "million", "billion", "trillion"]

    res = ""

    while number != 0:
        res = ((transrateBitween0To999(number % 1000) + " " +
                levels[levelInd]) + " " if number % 1000 != 0 else "") + res
        levelInd += 1
        number //= 1000

    return res[:-1]


def transrateIntToEnglish(number):

    if number >= 1000:
        return transrateOver1000((number // 1000)) + ("" if number % 1000 == 0 else " " + transrateBitween0To999(number % 1000))
    else:
        return transrateBitween0To999(number % 1000)


class Test(unittest.TestCase):
    def test_transrateIntToEnglish(self):
        self.assertEqual(transrateIntToEnglish(0), "zero")
        self.assertEqual(transrateIntToEnglish(1), "one")
        self.assertEqual(transrateIntToEnglish(8), "eight")
        self.assertEqual(transrateIntToEnglish(15), "fifteen")
        self.assertEqual(transrateIntToEnglish(92), "ninety two")
        self.assertEqual(transrateIntToEnglish(113),
                         "one hundred thirteen")

        self.assertEqual(transrateIntToEnglish(1001), "one thousand one")
        self.assertEqual(transrateIntToEnglish(
            2075), "two thousand seventy five")
        self.assertEqual(transrateIntToEnglish(20066),
                         "twenty thousand sixty six")
        self.assertEqual(transrateIntToEnglish(500012),
                         "five hundred thousand twelve")
        self.assertEqual(transrateIntToEnglish(950000),
                         "nine hundred fifty thousand")
        self.assertEqual(transrateIntToEnglish(1000000), "one million")
        self.assertEqual(transrateIntToEnglish(6000000000), "six billion")
        self.assertEqual(transrateIntToEnglish(2006000001),
                         "two billion six million one")
        self.assertEqual(transrateIntToEnglish(6020000000),
                         "six billion twenty million")
        self.assertEqual(transrateIntToEnglish(3000000000042),
                         "three trillion forty two")


if __name__ == "__main__":
    unittest.main()
