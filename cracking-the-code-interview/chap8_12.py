import copy


def findAvailableCol(posField, low, column):
    # 同じ列にあるかどうか
    lowFlg = False
    for prevlow in range(low):
        if posField[prevlow][column] == 1:
            lowFlg = True
    if lowFlg:
        return False

        # 斜めにあるかどうか
    nanameFlg = False
    for prevlow in range(low):
        for colOnPrevlow in range(8):
            if posField[prevlow][colOnPrevlow] == 1:
                if abs(column - colOnPrevlow) == abs(low - prevlow):
                    nanameFlg = True

    if nanameFlg:
        return False

    return True


def placeQueens(posField, row, res):
    if row == len(posField):
        res.append(copy.deepcopy(posField))
        return
    for column in range(len(posField)):
        if findAvailableCol(posField, row, column):
            posField[row][column] = 1
            placeQueens(posField, row + 1, res)
        posField[row][column] = 0


def calculate8QueenPos():
    posField = [[0 for _i in range(8)] for _j in range(8)]
    res = []
    placeQueens(posField, 0, res)
    return res


res = calculate8QueenPos()

for f in res:
    for low in f:
        print(low)
    print("")
