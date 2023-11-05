import deck
import player
import random

def pull_random_cards():
    return random.choice(deck)

def starting_turn(player1, player2):
    if player1.won_previous_hand:
        player1.can_play = False
        return player1
    else:
        player2.can_play = True
        return player2

class Game_Setup:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self._deck = deck.Deck()

    @property
    def deck(self):
        return self._deck
    
    def setup_game(self):
        try:
            # Check who is the dealer
            if self.player1.is_dealer:
                dealer = self.player1
                non_dealer = self.player2
            else:
                dealer = self.player2
                non_dealer = self.player1
            
            # Deal six cards in an alternating fashion, starting with the non-dealer
            for i in range(6):
                if i % 2 == 0:
                    non_dealer.hand.append(self.deck.draw_card())
                else:
                    dealer.hand.append(self.deck.draw_card())

            # Draw the 7th card and set its suit as the main suit for the deck
            trump_card = self.deck.draw_card()
            self.deck.main_suit = trump_card.suit
        except ValueError as e:
            print("Something went wrong during dealing")

def take_inputs():
    # Ask Names
    player1_name = input("Enter Name for Player 1: ")
    player2_name = input("Enter Name for Player 2: ")

    # Choose random player to call the color to determine who starts
    chosen_player = random.choice([player1_name, player2_name])
    while True:
        input_choice = input(f"{chosen_player} call a color \n1 Red \n2 Black \nEnter: ")
        if input_choice == '1':
            chose_black = True
            break  # Exit the loop
        elif input_choice == '2':
            chose_black = False
            break  # Exit the loop
        else:
            print("Invalid input. Please enter either 1 or 2.")
    # Create Players
    player1 = player.Player(player1_name, chose_black, False, False)
    player2 = player.Player(player2_name, not chose_black, False, False)
    
    # Assign chosen player based on name
    chosen_player = player1 if chosen_player == player1_name else player2
    other_player = player2 if chosen_player == player1_name else player1

    # Start a game
    game = Game_Setup(player1, player2)
    game.setup_game()

    # Pull a card from the middle of the deck (After dealing)
    start_color_call = random.choice(game.deck.cards)

    # Determine the starting player
    if start_color_call.suit in ["Spade", "Clubs"] and chose_black:
        chosen_player.won_previous_hand = True
        other_player.won_previous_hand = False
    elif start_color_call.suit in ["Hearts", "Diamonds"] and not chose_black:
        chosen_player.won_previous_hand = True
        other_player.won_previous_hand = False
    else:
        chosen_player.won_previous_hand = False
        other_player.won_previous_hand = True
    
    #print("Setup Finished") # Test

take_inputs()