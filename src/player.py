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

#        total_squares = 15
        # new
        ships_left = [5, 4, 3, 3, 2, 2, 1]

        # changed        
        while len(ships_left) != 0:
            print('{} please place your ships'.format(self.name))
#            print('{} cells remaining'.format(total_squares))
            print('You have ships of length {} left to place'.format(ships_left))
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
                    
                    # to check if inputs are valid numbers
                    if x < 0 or x > 11 or y_start < 0 or y_start > 11 or y_end < 0 or y_end > 11:
                        print('Invalid coordinates given. Please try again.')
                        continue

                    if y_end < y_start:
                        print('Invalid start and end, please ensure end-point is larger than start-point')
                        continue
                    
                    # to check if length is valid
                    ship_length = abs(y_start-y_end)+1
                    if ships_left.count(ship_length) == 0:
                        print('Invalide ship length. Please try again.')
                        continue
                    
                    #new to check if overlap
                    V_break = False
                    for i in range(y_start, y_end+1):
                        if self.board[i][x] == 1:
                            print('Your ships overlap. Please try placing it elsewhere. \n')
                            V_break = True
                            break
                    
                    if V_break:
                        continue

                    for i in range(y_start, y_end + 1):
                        self.board[i][x] = 1
                        
                    ships_left.remove(ship_length)
                except Exception:
                    print(Exception)

            elif direction == 'H':
                try:
                    y = int(input('Y-coordinate: '))
                    x_start = int(input('Starting X-coordinate: '))
                    x_end = int(input('Ending X-coordinate: '))
                    
                    # to check if inputs are valid numbers
                    if y < 0 or y > 11 or x_start < 0 or x_start > 11 or x_end < 0 or x_end > 11:
                        print('Invalid coordinates given. Please try again.')
                        continue
                    
                    if x_end < x_start:
                        print('Invalid start and end, please ensure end-point is larger than start-point')
                        continue

                    # to check if length is valid
                    ship_length = abs(x_start-x_end)+1
                    if ships_left.count(ship_length) == 0:
                        print('Invalide ship length. Please try again.')
                        continue
                    
                    #new to check if overlap                    
                    H_break = False
                    for i in range(x_start, x_end+1):
                        if self.board[y][i] == 1:
                            print('Your ships overlap. Please try placing it again. \n')
                            H_break = True
                            break
                    
                    if H_break:
                        continue

                    for i in range(x_start, x_end + 1):
                        self.board[y][i] = 1
                    
                    ships_left.remove(ship_length)
                except Exception:
                    print(Exception)
#            print(total_squares)
            self.print_board()
