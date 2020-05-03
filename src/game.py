#   Main
#
#   Battle-Py!
#
#   Authors: Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin
#
#


from player import Player
from bot import Bot


def play_game(player, bot):
    
    while (Win==False):
        player.make_guess(int(input('Enter X Coordinate: ')), int(input('Enter Y Coordinate: ')), bot)
        bot.take_guess(player)
        player.print_board()
        bot.print_board()


def main():
    player = Player(input('Enter your name: '))
    player.create_board(testing=True)
    
    bot = Bot(player)
    bot.print_board()

    play_game(player, bot)

if __name__ == '__main__':
    main()



#bug: using the game play V x = 2,5 y start = 1 y end = 4 only changes the first two spots not all 4
# update: the whole middle of the board doesn't change
