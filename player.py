import deck 
import constants

class Player:
    def __init__(self, name, start_choice, is_ai=False, won_previous_hand = False):
        # Formalities
        self.name = name
        self.is_ai = is_ai
        self._start_choice = start_choice


        # Dealing / Drawing 
        self._won_previous_hand = won_previous_hand
        self._is_dealer = constants.is_dealer(won_previous_hand)
        self._can_play = not won_previous_hand

        # Hand
        self.hand = []

        # Calculations
        self.cards_taken = []
        self.known_score = 0
        
        
    def show_hand(self):
        print(f"Current hand of {self.name} is:")
        i = 1
        for card in self.hand:
            print("\t",i, card)
            i += 1

    def known_score(self):
        return sum(constants.get_value(card) for card in self.cards_taken)

    def play(self, play):
        if 0 < play < constants.MAX_CARDS_IN_HAND:
            # Sort the indices in descending order to avoid index shifting
            sorted_indices = sorted(play, reverse=True)
            # Pop items based on sorted indices
            popped_items = [self.hand.pop(i) for i in play]
            # Return the items in the original order
            return popped_items[::-1]
        else:
            raise ValueError("Invalid amount of card to play requested")

    @property
    def is_dealer(self):
        return self._is_dealer
    @is_dealer.setter
    def is_dealer(self, value):
        _is_dealer = value
   
    @property
    def can_play(self):
        return self._can_play
    @can_play.setter
    def can_play(self, value):
        self._can_play = value

    @property
    def won_previous_hand(self):
        return self._won_previous_hand
    @won_previous_hand.setter
    def won_previous_hand(self, value):
        self._won_previous_hand = value