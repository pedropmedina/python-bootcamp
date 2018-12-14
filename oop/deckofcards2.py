# In this version, a trade off is made in the __init__() of each
# subclass of the Card superclass.

# Even tough, there is a trade off in adding more complexity to the __init__
# in the subclass for simplying the factory function just a bit, I personally,
# find this implementation clearer
class Card:
    def __init__(self, rank, suit, soft, hard):
        self.rank = rank
        self.suit = suit
        self.soft = soft
        self.hard = hard


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__('A', suit, 1, 11)


class FaceCard(Card):
    def __init__(self, rank, suit):
        chosen_rank = {11: 'J', 12: 'Q', 13: 'K'}.get(rank)
        super().__init__(chosen_rank, suit, 10, 10)


class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


def card(rank, suit):
    if rank == 1:
        return AceCard(rank, suit)
    elif 2 <= rank <= 10:
        return NumberCard(rank, suit)
    elif 11 <= rank <= 13:
        return FaceCard(rank, suit)
    else:
        raise Exception('Rank out of range')


Club, Diamond, Heart, Spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

deck = [
    card(rank, suit)
    for rank in range(1, 14)
    for suit in (Club, Diamond, Heart, Spade)
]

for d in deck:
    print(d.rank, d.suit.name, d.suit.symbol, d.soft, d.hard)
