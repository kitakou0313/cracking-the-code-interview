import unittest


def calculateNumOfHowManyCoinsHelper(n, usableCoins,  coinInd, memo):
    if n == 0:
        return 1

    if len(usableCoins) - 1 == coinInd:
        return 1

    if memo[coinInd][n] != -1:
        return memo[coinInd][n]

    ways = 0
    for coinNum in range(n // usableCoins[coinInd] + 1):
        if n - coinNum * usableCoins[coinInd] < 0:
            break
        ways += calculateNumOfHowManyCoinsHelper(
            n - coinNum*usableCoins[coinInd], usableCoins, coinInd + 1, memo)

    memo[coinInd][n] = ways
    return ways


def calculateNumOfHowManyCoins(n):
    usableCoins = [25, 10, 5, 1]

    memo = [[-1 for _i in range(n+1)] for _j in range(len(usableCoins))]

    coinInd = 0
    ways = 0
    for coinNum in range(n // usableCoins[coinInd] + 1):
        if n - coinNum * usableCoins[coinInd] < 0:
            break
        ways += calculateNumOfHowManyCoinsHelper(
            n - coinNum*usableCoins[coinInd], usableCoins, coinInd + 1, memo)

    return ways


class Test(unittest.TestCase):
    def test_coins1(self):
        self.assertEqual(calculateNumOfHowManyCoins(0), 1)
        self.assertEqual(calculateNumOfHowManyCoins(1), 1)
        self.assertEqual(calculateNumOfHowManyCoins(4), 1)
        self.assertEqual(calculateNumOfHowManyCoins(5), 2)
        self.assertEqual(calculateNumOfHowManyCoins(15), 6)
        self.assertEqual(calculateNumOfHowManyCoins(17), 6)
        self.assertEqual(calculateNumOfHowManyCoins(20), 9)
        self.assertEqual(calculateNumOfHowManyCoins(25), 13)
        self.assertEqual(calculateNumOfHowManyCoins(52), 49)


if __name__ == "__main__":
    unittest.main()
