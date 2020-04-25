# Main
#
# Battle-Py!
#
# Authors: Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin
#
#


from player import Player
from bot import Bot


def play_game(player, bot):
    player.create_board()
    bot.print_board()

    while player_win(player) == False: # and bot_win(bot) == False:
        player.make_guess(int(input('Enter X Coordinate: ')), int(input('Enter Y Coordinate: ')), bot)
        player.print_board()
        bot.print_board()
    
    
def player_win(player):
    for i in player.ships:
        if i.sunk == False:
            return False
    return True

# uncomment when bot class is done and has a ships attribute
#def bot_win(bot):
#    for i in bot.ships:
#        if i.sunk == False:
#            return False
#    return True

def main():
    player = Player(input('Enter your name: '))
    bot = Bot()

    play_game(player, bot)

if __name__ == '__main__':
    main()

