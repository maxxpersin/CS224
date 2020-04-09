#
#
#   Bot Class
#
#

class Bot:
    def __init__(self):
        self.hidden_board = [0] * 12
        self.clean_board = [0] * 12
        for i in range(0, len(self.clean_board)):
            self.hidden_board[i] = [0] * 12
            self.clean_board[i] = ['X'] * 12

    
    def print_board(self):
        print('Opponents Board:')
        for i in range(0, len(self.clean_board)):
            print(self.clean_board[i])
    
    def get_hidden_board(self):
        return self.hidden_board

    def update_clean_board(self, x, y):
        self.clean_board[x][y] = self.hidden_board[x][y]