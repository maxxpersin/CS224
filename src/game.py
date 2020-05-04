#   Main
#
#   Battle-Py!
#
#   Authors: Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin
#
#


from player import Player
from bot import Bot
import sys


def check_win(player, bot):
    return bot.all_ships_sunk()


def play_game(player, bot, testing=False):
    Win = False
    while (Win == False):
        try:
            player.make_guess(int(input('Enter X Coordinate: ')),
                              int(input('Enter Y Coordinate: ')), bot)
        except Exception:
            print('X and Y must be numbers')
            continue
        bot.take_guess(player)
        player.print_board()
        if testing == True:
            bot.print_board_cheat()
        bot.print_board()

        Win = check_win(player, bot)
    
    print('YOU WIN!')


def main(args):
    if len(args) > 1:
        if args[1] == 'test':
            testing = True
        else:
            testing = False
    else:
        testing = False

    player = Player(input('Enter your name: '))
    player.create_board(testing=testing)

    bot = Bot(player)
    if testing == True:
        bot.print_board_cheat()
    bot.print_board()

    play_game(player, bot, testing=testing)


if __name__ == '__main__':
    main(sys.argv)

# bug: using the game play V x = 2,5 y start = 1 y end = 4 only changes the first two spots not all 4
# update: the whole middle of the board doesn't change
