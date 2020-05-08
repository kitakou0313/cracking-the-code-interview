s1 = input("String 1 ")


def isOdd(s1):
    dic = {}
    for c in s1:
        if c in dic:
            return False
        dic[c] = 1
    return True


print(isOdd(s1))
