import constants
import card

def card_vs_card(placed_card, card, main_suit):
    placed_rank = placed_card.rank
    placed_suit = placed_card.suit
    rank = card.rank
    suit = card.suit
    if (suit == main_suit and (placed_suit != main_suit or constants.get_value(rank) > constants.get_value(placed_rank))) or (suit == placed_suit and constants.get_value(rank) > constants.get_value(placed_rank)):
        return True
    else:
        return False


def can_beat_placed(placed_cards, hand, main_suit):
    # Create a copy of the hand to modify
    remaining_hand = hand[:]
    
    # Sort the remaining hand by rank, with the main suit cards being treated as highest
    remaining_hand.sort(key=lambda card: (card.suit == main_suit, constants.get_value(card.rank)), reverse=True)

    # List to store the pairs of cards
    card_pairs = []


    # Iterate through the placed cards
    for placed_card in placed_cards:
        can_beat = False
        card_to_remove = None

        # Iterate through the remaining cards in hand
        for card in remaining_hand:
            
            # Check if the card is of the main suit or higher rank of the same suit
            if card_vs_card(placed_card, card):
                can_beat = True
                card_to_remove = card
                card_pairs.append((placed_card, card))
                # Break after finding the least valuable card that can defeat the placed card
                break
        
        # If any placed card cannot be beaten, return False
        if not can_beat:
            return False, []
        else:
            # Remove the used card from the remaining hand
            remaining_hand.remove(card_to_remove)
    
    # If all placed cards can be beaten, return True
    return True, card_pairs

def give_card(hand, card):
    card.is_hidden(True)
    hand.remove(hand)