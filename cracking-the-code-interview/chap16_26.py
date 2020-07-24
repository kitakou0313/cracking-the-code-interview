import unittest
import math


def calculate(string):
    opeAndPriorityDic = {"+": 0, "-": 0, "*": 1, "/": 1}
    numSet = set([str(i) for i in range(0, 10)])

    def collapseSrack(numberStack, operatorStack):
        operator = operatorStack.pop()
        number2 = numberStack.pop()
        number1 = numberStack.pop()

        if operator == "+":
            numberStack.append(number1 + number2)
        elif operator == "-":
            numberStack.append(number1 - number2)
        elif operator == "*":
            numberStack.append(number1 * number2)
        elif operator == "/":
            numberStack.append(math.floor(number1 / number2))

    def parseStringToNum(string, ind):
        resNum = ""
        while ind < len(string) and string[ind] in numSet:
            resNum += string[ind]
            ind += 1

        return int(resNum), ind-1

    numberStack = []
    operatorStack = []

    ind = 0
    while ind < len(string):
        if string[ind] in numSet:
            num, ind = parseStringToNum(string, ind)
            numberStack.append(num)
        else:
            if len(operatorStack) == 0:
                operatorStack.append(string[ind])
            elif opeAndPriorityDic[string[ind]] <= opeAndPriorityDic[operatorStack[-1]]:
                collapseSrack(numberStack, operatorStack)
                operatorStack.append(string[ind])
            else:
                operatorStack.append(string[ind])

        ind += 1

    while len(operatorStack) != 0:
        collapseSrack(numberStack, operatorStack)

    return numberStack[-1]


class Test(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate("1+1"), 2)
        self.assertEqual(calculate("0+4"), 4)
        self.assertEqual(calculate("0*7"), 0)
        self.assertEqual(calculate("9*0+1"), 1)
        self.assertEqual(calculate("1+1+1"), 3)
        self.assertEqual(calculate("1+6/5"), 2)
        self.assertEqual(calculate("3+7/8*7"), 3)
        self.assertEqual(calculate("1+11"), 12)
        self.assertEqual(calculate("200+423"), 623)


if __name__ == "__main__":
    unittest.main()
