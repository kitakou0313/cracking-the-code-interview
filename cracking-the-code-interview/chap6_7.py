import random


def calBirthRate(numOfPeople):
    people = ["M" if random.randrange(
        2) == 0 else "W" for n in range(numOfPeople)]
    man = 0
    women = 0
    for person in people:
        if person == "M":
            man += 1
        else:
            women += 1

    return women / man


for x in [100, 10000, 100000]:
    print(calBirthRate(x))
