#
#   Player class
#
#


class Player():
    def __init__(self, name):
        self.name = name
        self.board = [0] * 12
        for i in range(0, len(self.board)):
            self.board[i] = [0] * 12
        
        self.board[0][9] = 1
    
    def get_board(self):
        return self.board

    def print_board(self):
        print("{}'s Board:".format(self.name))
        for i in range(0, len(self.board)):
            print(self.board[i])

    def make_guess(self, x, y, opponent):
        opponent.update_clean_board(x, y)
            
    

