# Main
#
# Battle-Py!
#
# Authors: Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin
#
#

from tkinter import *
from player import Player
from bot import Bot


def play_game(player, bot):
    player.print_board()
    bot.print_board()

    player.make_guess(int(input('Enter X Coordinate: ')), int(input('Enter Y Coordinate')), bot)
    player.print_board()
    bot.print_board()


def main():
    player = Player(input('Enter your name: '))
    bot = Bot()

    play_game(player, bot)

if __name__ == '__main__':
    main()
