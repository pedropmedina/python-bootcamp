from functools import partial


# Card will work as a superclass
# rank and suit are assigned as argument values to the class
# hard and soft will be assigned from an instance method using
# polymorphism
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()

    # define _points() method here to avoid error in pylint
    # This method will be overriden by the subclasses' implementation
    # of _points. Since we never instantiate Class directly, we'll never
    # have to worry about _points here. If we want to call _points in the
    # superclass for the subclass, we can use super()._points()
    def _points(self):
        return None, None


# Below are the types of cards:
# The three subclasses provide a unique implementation of
# _points() method. All subclasses have idential signatures having the
# same mathods and attributes. This is an example of polymorphism
class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10


# Let's make suite an object that will allow for more complex design
class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


# Instantiating each suit
Club, Diamond, Heart, Spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# factory function versions:

# V1 includes mapping with conditions all together which is not best practice
def card_v1(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception('Rank out of range')


# V2 separates mapping and leaves all conditions.
#  Better solution, but a bit verbose
def card_v2(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank:
        return FaceCard('J', suit)
    elif 12 <= rank:
        return FaceCard('Q', suit)
    elif 13 <= rank:
        return FaceCard('K', suit)
    else:
        raise Exception('Rank out of range')


# V3 maps to a tuple. When we call get() on the dictionary, and pass it
# a default of NumberCard class in case rank is 2 < 11, we get back
# a tuple of (class, rank) which gets unpack into class_, and rank_str.
# Finally we return the instantiated class
def card_v3(rank, suit):
    class_, rank_str = {
        1: (AceCard, 'A'),
        11: (FaceCard, 'J'),
        12: (FaceCard, 'Q'),
        13: (FaceCard, 'K'),
    }.get(rank, (NumberCard, str(rank)))
    return class_(rank_str, suit)


# In this case we use partial() method from functools. This version
# is unecessary partial does not help much in this specific example
def card_v4(rank, suit):
    partial_class = {
        1: partial(AceCard, 'A'),
        11: partial(FaceCard, 'J'),
        12: partial(FaceCard, 'Q'),
        13: partial(FaceCard, 'K'),
    }.get(rank, partial(NumberCard, str(rank)))
    return partial_class(suit)


# In this version we use a fluent factory object that works very much
# like partial in the sense that it keeps state around for use in its methods.
# in a fluent factory object we can chain methods and share state among
# them while keeping method organized in one place
class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))
        return self  # returnig self will allows to chain of this object

    def suit(self, suit):
        return self.class_(self.rank_str, suit)


deck = [
    CardFactory().rank(rank).suit(suit)
    for rank in range(1, 14)
    for suit in (Club, Diamond, Heart, Spade)
]

for d in deck:
    print(d.rank, (d.suit.name, d.suit.symbol), d.soft, d.hard)
