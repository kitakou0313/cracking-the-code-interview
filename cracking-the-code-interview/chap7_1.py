import unittest
import copy


class Card():
    def __init__(self, val, suit):
        self.__val, self.__suit = val, suit

    def getSuit(self):
        return self.__suit

    def getVal(self):
        return self.__val


class CardDeck():
    def __init__(self, cards=None):
        self.cards = cards

    def drawCard(self):
        return self.cards.pop()


class BlackjackHand(CardDeck):

    def calValue(self):
        vals = [0]
        for card in self.cards:
            if card.getVal() == 1:
                vals1 = copy.copy(vals)
                vals2 = copy.copy(vals)

                for i in range(len(vals)):
                    vals1[i] += 1
                    vals2[i] += 11

                vals = copy.copy(vals1 + vals2)

            else:
                for i in range(len(vals)):
                    vals[i] += card.getVal()
        res = -1
        for val in vals:
            if val <= 21:
                res = max(res, val)

        return res


class Test(unittest.TestCase):
    def test_card_deck(self):
        deck = CardDeck([Card(2, "Hearts"), Card(4, "Clubs")])
        self.assertEqual(deck.drawCard().getSuit(), "Clubs")

    def test_blackjack_hand(self):
        hand = BlackjackHand([Card(5, "Diamonds"), Card(7, "Clubs")])
        self.assertEqual(hand.calValue(), 12)
        hand = BlackjackHand([Card(5, "Diamonds"), Card(1, "Clubs")])
        self.assertEqual(hand.calValue(), 16)
        hand = BlackjackHand([Card(12, "Diamonds"), Card(1, "Clubs")])
        self.assertEqual(hand.calValue(), 13)
        hand = BlackjackHand(
            [Card(12, "Diamonds"), Card(1, "Clubs"), Card(1, "Hearts")])
        self.assertEqual(hand.calValue(), 14)


if __name__ == "__main__":
    unittest.main()
