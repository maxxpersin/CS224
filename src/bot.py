#
#
#   Bot Class
#
#
from termcolor import colored

class Bot:
    def __init__(self):
        self.hidden_board = [0] * 12
        self.clean_board = [0] * 12
        for i in range(0, len(self.clean_board)):
            self.hidden_board[i] = [0] * 12
            self.clean_board[i] = ['X'] * 12

    
    def print_board(self):
        print('Opponents Board:')
#        for i in range(0, len(self.clean_board)):
#            print(self.clean_board[i])
        
        # should make the board look pretty now
        for i in range(0, len(self.clean_board)):
            for j in range(0, len(self.clean_board[i])):
                if self.clean_board[i][j] == 1:
                    print(colored(str(self.clean_board[i][j]), 'red'), end=' ')
                else:
                    print(self.clean_board[i][j], end=' ')
            print()
    
    def get_hidden_board(self):
        return self.hidden_board

    def update_clean_board(self, x, y):
        self.clean_board[x][y] = self.hidden_board[x][y]