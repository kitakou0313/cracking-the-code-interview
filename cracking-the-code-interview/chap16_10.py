import unittest


class P():
    def __init__(self, birthY, deadY=None):
        self.birthY = birthY
        self.deadY = deadY


def findMostNumberOfPeopleLiving(people):
    yearDArray = [0 for i in range(101)]  # 1900 ~ 2000
    peopleNumArray = [0 for i in range(102)]  # 1899 ^ 2000

    for person in people:
        yearDArray[person.birthY - 1900] += 1
        if person.deadY is None:
            continue
        yearDArray[person.deadY - 1900] -= 1

    for ind in range(1, len(peopleNumArray)):
        peopleNumArray[ind] = peopleNumArray[ind - 1] + yearDArray[ind - 1]

    ans = (-1, 0)  # Peope, year

    for ind in range(1, len(peopleNumArray)):
        ans = (peopleNumArray[ind],
               ind) if ans[0] < peopleNumArray[ind] else ans

    return 1900 + ans[1] - 1


class Test(unittest.TestCase):
    def test_most_living_people(self):
        people = [P(1907, 1942), P(1909, 1982), P(
            1933, 1967), P(1912, 1954), P(1980), P(1988)]
        self.assertEqual(findMostNumberOfPeopleLiving(people), 1933)


if __name__ == "__main__":
    unittest.main()
