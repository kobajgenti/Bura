import player
import game_setup
import card_interactions as ci
import card

# TEST CODE game_setup
koba_p = player.Player("Koba", "Black", False, True)
gio_p = player.Player("Gio", "Red", False, False)

test_game = game_setup.Game_Setup(koba_p, gio_p)
test_game.setup_game()
test_game.player1.show_hand()
test_game.player2.show_hand()
print(test_game.deck.main_suit)

# TEST CODE card_interactions
placed_cards = [card.Card('Ten', 'Diamonds'), card.Card('Queen', 'Spades')]
hand = [card.Card('Ace', 'Diamonds'), card.Card('Ten', 'Clubs'), card.Card('King', 'Spades', True)]
main_suit = 'Diamonds'

result, card_pairs = ci.can_beat_placed(placed_cards, hand, main_suit)

if result:
    print("True, Cards to use for defeating:")
    for placed, hand_card in card_pairs:
        print(f"Use {hand_card} to defeat {placed}")
else:
    print("False, cannot defeat all placed cards.")