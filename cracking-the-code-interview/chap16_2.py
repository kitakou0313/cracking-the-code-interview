import unittest


class stat():
    def __init__(self):
        self.total_words = 0
        self.dicOfWordsNum = {}

    def getFreqOfWord(self, word):
        return self.dicOfWordsNum[word] / self.total_words


def calFrequencyOfEachWords(document):

    document = document.replace("\n", " ").replace(
        "(", "").replace(")", "").lower().split(" ")

    document = [word for word in document if word != ""]

    stats = stat()

    for word in document:

        stats.total_words += 1
        if word not in stats.dicOfWordsNum:
            stats.dicOfWordsNum[word] = 0

        stats.dicOfWordsNum[word] += 1

    return stats


class Test(unittest.TestCase):
    def test_word_frequency(self):
        text = """When the sun shines, we'll shine together
        Told you I'd be here forever
        Said I'll always be a friend
        Took an oath I'ma stick it out 'til the end
        Now that it's raining more than ever
        Know that we'll still have each other
        You can stand under my umbrella
        You can stand under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh eh eh eh)"""
        stats = calFrequencyOfEachWords(text)
        self.assertEqual(stats.total_words, 87)
        self.assertEqual(stats.getFreqOfWord("umbrella"), 5 / 87.0)


if __name__ == "__main__":
    unittest.main()
