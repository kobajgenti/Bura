POSSIBLE_RANKS = ["Jack", "Queen", "King", "Ten", "Ace"]
POSSIBLE_SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]

def get_value(rank):
    if rank == "Jack":
        return 2
    elif rank == "Queen":
        return 3
    elif rank == "King":
        return 4
    elif rank == "Ten":
        return 10
    elif rank == "Ace":
        return 11
    else: 
        raise ValueError("Invalid rank")
    
MAX_CARDS_IN_HAND = 3

def is_dealer(won):
    if won:
        return True
    else:
        return False