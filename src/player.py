#
#   Player class
#
#

from termcolor import colored


class Player():
    def __init__(self, name):
        self.name = name
        self.allow_board_creation = True
        self.board = [0] * 12
        for i in range(0, len(self.board)):
            self.board[i] = [0] * 12

    def get_board(self):
        return self.board

    def print_board(self):
        print("{}'s Board:".format(self.name))
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == 1:
                    print(colored(str(self.board[i][j]), 'red'), end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()

    def make_guess(self, x, y, opponent):
        opponent.update_clean_board(x, y)

    def create_board(self):
        if not self.allow_board_creation:
            return

        self.allow_board_creation = False

        self.print_board()

        total_squares = 15
        while total_squares > 0:
            print('{} please place your ships'.format(self.name))
            print('{} cells remaining'.format(total_squares))
            passed = False
            while not passed:
                direction = input('Ship orientation (V/H): ')
                if direction == 'V' or direction == 'H':
                    passed = True
                else:
                    print(
                        'Please specify V for vertical orientation or H for horizontal orientation')

            if direction == 'V':
                try:
                    x = int(input('X-coordinate: '))
                    y_start = int(input('Staring Y-coordinate: '))
                    y_end = int(input('Ending Y-coordinate: '))

                    for i in range(y_start, y_end + 1):
                        self.board[i][x] = 1
                        total_squares -= 1
                except Exception:
                    print(Exception)

            elif direction == 'H':
                try:
                    y = int(input('Y-coordinate: '))
                    x_start = int(input('Starting X-coordinate: '))
                    x_end = int(input('Ending X-coordinate: '))

                    for i in range(x_start, x_end + 1):
                        self.board[y][i] = 1
                        total_squares -= 1
                except Exception:
                    print(Exception)
            print(total_squares)
            self.print_board()
