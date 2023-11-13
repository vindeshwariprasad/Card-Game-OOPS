
class Suit:

    Sign = {"clubs": "♣", "diamonds": "♦", "hearts": "♥", "spades": "♠"}

    def __init__(self, brief):
        self._brief = brief
        self._symbol = Suit.Sign[brief.lower()]

    @property
    def brief(self):
        return self._brief

    @property
    def symbol(self):
        return self._symbol
