#
#
#   Bot Class
#
#
from random import randint


class Bot:
    def __init__(self, players):
        self.hidden_board = [0] * 12
        self.clean_board = [0] * 12
        self.guesses = [0]*12
        self.player_board = players.get_board()
        self.current = []
        for i in range(0, len(self.clean_board)):
            self.hidden_board[i] = [0] * 12
            self.clean_board[i] = ['X'] * 12
            self.guesses[i] = ['X'] * 12

        ships = [5, 4, 3, 3, 2]
        for x in ships:
            self.place_ship(x)
        self.print_board_cheat()

    def place_ship(self, x):
        dir = randint(0, 1)
        if dir == 0:
            # do vertical
            passed = 0
            start_x = randint(0, 11)
            start_y = randint(0, 11)
            while passed == 0:
                passed = 1
                for z in range(0, x):
                    if start_y+z > 11:
                        # if off board set to not pass and generate new randoms
                        passed = 0
                        start_x = randint(0, 11)
                        start_y = randint(0, 11)
                        break
                    if (self.hidden_board[start_x][(start_y+z)] == 1):
                        # if overlapped with another ship set to not pass and generate new randoms
                        passed = 0
                        start_x = randint(0, 11)
                        start_y = randint(0, 11)
                        break
            for z in range(0, x):
                self.hidden_board[start_x][(start_y+z)] = 1

        else:
            # do Horizontal
            passed = 0
            start_x = randint(0, 11)
            start_y = randint(0, 11)
            while passed == 0:
                passed = 1
                for z in range(0, x):
                    if start_x+z > 11:
                        # if off board set to not pass and generate new randoms
                        passed = 0
                        start_x = randint(0, 11)
                        start_y = randint(0, 11)
                        break
                    if (self.hidden_board[(start_x+z)][start_y] == 1):
                        # if overlapped with another ship set to not pass and generate new randoms
                        passed = 0
                        start_x = randint(0, 11)
                        start_y = randint(0, 11)
                        break
            for z in range(0, x):
                self.hidden_board[(start_x+z)][start_y] = 1

    def take_guess(self, player):
        if(len(self.current) == 0):
            guess_x = randint(0, 11)
            guess_y = randint(0, 11)
            while guesses[guess_x][guess_y] is 'X':
                guess_x = randint(0, 11)
                guess_y = randint(0, 11)
            print("bot guesses {} {}".format(guess_x, guess_y))
            guesses[guess_x][guess_y] = self.player_board[guess_x][guess_y]
            # DO guess
            self.current.insert(0, (guess_x, guess_y))

    def print_board(self):
        print('Opponents Board:')
        for i in range(0, len(self.clean_board)):
            print(self.clean_board[i])

    def print_board_cheat(self):
        for i in range(0, len(self.clean_board)):
            print(self.hidden_board[i])

    def get_hidden_board(self):
        return self.hidden_board

    def update_clean_board(self, x, y):
        self.clean_board[x][y] = self.hidden_board[x][y]
