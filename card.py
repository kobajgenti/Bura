# Imports
import random
import constants
from PIL import Image, ImageTk

class Card:
    # Constructor method with instance variables
    def __init__(self, rank, suit, is_main_suite = False, is_hidden =  False):
        self._suit = suit
        self._rank = rank
        self._value = constants.get_value(rank)
        self._is_main_suit = is_main_suite
        self._is_hidden = is_hidden
        self.image = Image.open(f"card_images/face/{rank}/{suit}.png")
        
    @property
    def value(self):
        return self._value
    @property
    def rank(self):
        return self._rank
    @property
    def suit(self):
        return self._suit
    
    @property
    def is_hidden(self):
        return self._is_hidden
    @is_hidden.setter
    def is_hidden(self, value):
        self._is_hidden = value


    @property
    def is_main_suit(self):
        return self._is_main_suit
    @is_main_suit.setter
    def is_main_suit(self, is_main_suit):
        self._is_main_suit = is_main_suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    