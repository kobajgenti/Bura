import random
import card
import constants

class Deck:
    # Constructor method with instance variables
    def __init__(self):
        self.cards = []
        self._main_suit = None
        for rank in constants.POSSIBLE_RANKS:
            for suit in constants.POSSIBLE_SUITS:
                self.cards.append(card.Card(rank, suit))
        random.shuffle(self.cards)

    @property
    def main_suit(self):
        if self._main_suit == None:
            print("Main suit not set")
        else: 
            return self._main_suit
    @main_suit.setter
    def main_suit(self, suit):
        if suit in constants.POSSIBLE_SUITS:
            self._main_suit = suit
            for card in self.cards:
                card.is_main_suit = (card.suit == suit)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise ValueError("All cards have been drawn")

    def cut_deck(self, cut_place):
        if 0 < cut_place <= len(self.cards):
            first_part = self.cards[:cut_place]
            second_part = self.cards[cut_place:]
            self.cards = second_part + first_part
        else: 
            raise ValueError("Invalid cut_place")
    
    def __str__(self):
        deck_comp = ''
        for card in self.cards:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp