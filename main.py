
from deck import Deck
from player import Player
from game import Game

player = Player("Vindy", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = Game(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nAre you ready for the next round?\nPress Enter to continue. Enter S to stop.")

    if answer.lower() == "s":
        break


