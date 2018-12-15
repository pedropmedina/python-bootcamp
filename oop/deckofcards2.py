import abc
import random

# Examples from Mastering Object-oriented Python

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

# composite objects

# using built in class
deck = [
    card(rank, suit)
    for rank in range(1, 14)
    for suit in (Club, Diamond, Heart, Spade)
]

# wrapping a collection class. This wrapper class simply keeps
# the list in one place by wrapping it and then delegating methods
# to it. This method can become a bit redundant compare to just using
# the built in list as shown above
class Deck2:
    def __init__(self):
        self._cards = [
            card(rank, suit)
            for rank in range(1, 14)
            for suit in (Club, Diamond, Heart, Spade)
        ]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()


# Extending a collection. Here we create a subclass of list itself.
# The list is initialize with super().__init__(). All methods from
# list will apply to the instance of this class. This method fixes the
# redundancy from Deck2
class Deck3(list):
    def __init__(self):
        super().__init__(
            card(rank, suit)
            for rank in range(1, 14)
            for suit in (Club, Diamond, Heart, Spade)
        )
        random.shuffle(self)


# Emulate casino blackjack as dealt from a shoe:
# Implementing multiple sets of 52 card decks. Instead of initializing list
# superclass, we start with an empty list super().__init__(), then, we
# extend the empty list to add as many desks as requested when the class
# is initialized [defaults to 1]. The list of desks is shuffle, and
# we select a burn number within the range 1, and 52 which is used to
# take some cards out of the game
class Deck4(list):
    def __init__(self, decks=1):
        super().__init__()
        for _ in range(decks):
            self.extend(
                card(rank, suit)
                for rank in range(1, 14)
                for suit in (Club, Diamond, Heart, Spade)
            )
            random.shuffle(self)
            burn = random.randint(1, 52)
            for _ in range(burn):
                self.pop()


# Hand description for emulating play strategies
class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def hard_total(self):
        return sum(c.hard for c in self.cards)

    def soft_total(self):
        return sum(c.soft for c in self.cards)


# Using static methods for initialization of Hand
class Hand1:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    @staticmethod
    def freeze(other):
        hand = Hand1(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1):
        hand0 = Hand1(other.dealer_card, other.cards[0], card0)
        hand1 = Hand1(other.dealer_card, other.cards[1], card1)
        return hand0, hand1

    def __str__(self):
        return ', '.join(map(str, self.cards))


# Stateless objects without __init__()
# Stateless objects are a common design pattern for Strategy objects
# Strategy object is plugged into a master object to implement algorithm
# decision that might rely in data from the master or any other data.
# Strategy objects is a collection of functions
class GameStrategy:
    def insurance(self, hand):
        return False

    def split(self, hand):
        return False

    def double(self, hand):
        return False

    def hit(self, hand):
        return sum(c.hard for c in hand.cards) <= 17


d = Deck4()


class Table:
    def __init__(self):
        self.deck = Deck4()

    def place_bet(self, amount):
        print('Bet', amount)

    def get_hand(self):
        try:
            self.hand = Hand(d.pop(), d.pop(), d.pop())
            self.hole_card = d.pop()
        except IndexError:
            # Out of cards: need to shuffle
            self.deck = Deck4()
            return self.get_hand()
        print('Deal', self.hand)

    def can_insure(self, hand):
        return hand.dealer_card.insure


# Abstract superclass
# It defines the methods with default values
# The subclass can override the methods or use them in the
# superclass if needed
class BettingStrategy:
    def bet(self):
        raise NotImplementedError('No bet method')

    def record_win(self):
        pass

    def record_loss(self):
        pass


# The abstract class can be formalized with the usage of the abc module
# The advantage of using abc module is that by using the abstractmethod
# decorator, we ensure that any subclass must define the bet method, otherwise
# an exception will be raised
# We still can access the bet() method in the superclass with super().bet()
class BettingStrategy1(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bet(self):
        return 1

    def record_win(self):
        pass

    def record_loss(self):
        pass


class Player:
    def __init__(self, table, bet_strategy, game_strategy):
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table = table

    def game(self):
        self.table.place_bet(self.bet_strategy.bet())
        self.hand = self.table.get_hand()
        if self.table.can_insure(self.hand):
            if self.game_strategy.insurance(self.hand):
                self.table.insurance(self.bet_strategy.bet())
