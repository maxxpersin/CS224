#
#
#   Bot Class
#
#
from random import randint
from termcolor import colored
from ship import Ship


class Bot:
    def __init__(self, players):
        self.hidden_board = [0] * 12
        self.clean_board = [0] * 12
        self.guesses = [0]*12
        self.hits_reamaining = 16
        self.ships = []
        self.player_board = players.get_board()
        self.current = []
        self.dir = -1
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
            new_ship = Ship(start_x, start_y, 'V', x, self.hidden_board)
            self.ships.append(new_ship)

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
            new_ship = Ship(start_x, start_y, 'H', x, self.hidden_board)
            self.ships.append(new_ship)

    def take_guess(self,player):
        #if a ship has not been found guess at random
        if(len(self.current) == 0):
            self.dir=-1
            guess_x=randint(0,11)
            guess_y=randint(0,11)
            while self.guesses[guess_x][guess_y] != 'X':
                #creates random guesses until an unguessed position is found
                guess_x=randint(0,11)
                guess_y=randint(0,11)
            self.guesses[guess_x][guess_y]=self.player_board[guess_x][guess_y]
            #DO guess
            player.update_board(guess_x,guess_y)
            if  self.guesses[guess_x][guess_y]==1:
                #if is hit record position for next guess
                self.hits_reamaining=self.hits_reamaining-1
                self.current.insert(0,(guess_x,guess_y))
        #if a ship is found but not a direction this area is called
        elif (len(self.current)==1):
            g=-1
            g2=-1
            #checks if possible guesses have been taken
            if self.is_ship_final():
                self.current=[]
                self.take_guess(player)
                return
            #finds a random unguessed adjacent space
            while g2==-1 or self.guesses[g][g2]!='X':
                if(self.dir_change==False):
                    temp_dir=randint(0,3)
                else:
                    temp_dir=self.dir
                    self.dir_change=False
                if temp_dir==0:
                    g=self.current[0][0]
                    g2=self.current[0][1]
                    g=g+1
                    if g>11:
                        g2=-1
                if temp_dir==1:
                    g=self.current[0][0]
                    g2=self.current[0][1]
                    g2=g2+1
                    if g2>11:
                        g2=-1
                if temp_dir==2:
                    g=self.current[0][0]
                    g2=self.current[0][1]
                    g=g-1
                    if g<0:
                        g2=-1
                if temp_dir==3:
                    g=self.current[0][0]
                    g2=self.current[0][1]
                    g2=g2-1
                    if g2<0:
                        g2=-1
            if(player.get_board()[g][g2]=='X' or player.get_board()[g][g2]=='O' or not self.in_bounds(g,g2)):
                self.current=[]
                self.take_guess(player)
                return
            self.guesses[g][g2]=player.get_board()[g][g2]
            player.update_board(g,g2)
            #if it is a hit saves the location
            if self.guesses[g][g2]==1:
                self.hits_reamaining=self.hits_reamaining-1
                self.current.insert(0,(g,g2))
                self.dir=temp_dir
        #if there is a position and direction found this handles the guesses
        else:
            #heads right
            if self.dir==0:
                g=self.current[0][0]
                g2=self.current[0][1]
                g=g+1
            #heads down
            elif self.dir==1:
                g=self.current[0][0]
                g2=self.current[0][1]
                g2=g2+1
            #heads left
            elif self.dir==2:
                g=self.current[0][0]
                g2=self.current[0][1]
                g=g-1
            #heads right
            elif self.dir==3:
                g=self.current[0][0]
                g2=self.current[0][1]
                g2=g2-1
            #if it is a valid guess then do the guess
            if self.guesses[g][g2]=='X' and self.in_bounds(g,g2):
                self.guesses[g][g2]=self.player_board[g][g2]
                player.update_board(g,g2)
                #if it is a hit store the position
                if self.guesses[g][g2]==1:
                    self.hits_reamaining=self.hits_reamaining-1
                    self.current.insert(0,(g,g2))
                    print(self.current)
                #if it is a miss clear back to the first hit on this ship
                else:
                    while len(self.current)>1:
                        self.current.pop(0)
                    self.dir_change=True
                    #changes to force the opposite direction
                    self.dir_change=True
                    if self.dir==0:
                        self.dir=2
                    elif self.dir==1:
                        self.dir=3
                    elif self.dir==2:
                        self.dir=0
                    elif self.dir==3:
                        self.dir=1
            #if the next space has been guessed then check the other direction
            else:
                while len(self.current)>1:
                   self.current.pop(0)
                   print(self.current)
                self.dir_change=True
                if self.dir==0:
                   self.dir=2
                elif self.dir==1:
                   self.dir=3
                elif self.dir==2:
                   self.dir=0
                elif self.dir==3:
                   self.dir=1
                self.take_guess(player)
        self.win()

    #confirms neither bound is out of the array
    def in_bounds(self, g, g2):
        if g > -1 and g < 12:
            if g2 > -1 and g2 < 12:
                return True
        return False
    #prints the board that the player would see
    def print_board(self):
        print('Opponents Board:')
        for i in range(0, len(self.clean_board)):
            for j in range(0, len(self.clean_board[i])):
                if self.clean_board[i][j] == 1:
                    print(colored(str(self.clean_board[i][j]), 'red'), end=' ')
                elif self.clean_board[i][j] == 0:
                    print(
                        colored(str(self.clean_board[i][j]), 'blue'), end=' ')
                else:
                    print(self.clean_board[i][j], end=' ')
            print()
    #prints a unhidden board
    def print_board_cheat(self):
        for i in range(0, len(self.clean_board)):
            print(self.hidden_board[i])
    #prints the hidden board the bot would see
    def print_guesses(self):
        for i in range(0, len(self.clean_board)):
            print(self.guesses[i])
    #returns the current state of the board hidding unguessed positions
    def get_hidden_board(self):
        return self.hidden_board

    def update_clean_board(self, x, y):
        self.clean_board[x][y] = self.hidden_board[x][y]
        if self.clean_board[x][y] == 1:
            for ship in self.ships:
                ship.hit(y, x)

    def all_ships_sunk(self):
        num_ships = len(self.ships)
        count = 0
        for ship in self.ships:
            if ship.is_ship_sunk():
                count += 1
        return count == num_ships
    #if every player ship position has been hit end the game, the bot wins
    def win(self):
        if self.hits_reamaining == 0:
            print("YOU LOOSE, Better Luck Next time.")
            quit()
    #checks if there is a possible guess
    def is_ship_final(self):
         t=self.current[0][0]
        y=self.current[0][1]
        count=0
        if(self.dir==0 or self.dir==2):
            print('x')
            if t!=0:
                if self.guesses[t-1][y]=='X':
                    return False
            if t!=11:
                if self.guesses[t+1][y]=='X':
                    return False
        elif(self.dir==1 or self.dir==3):
            print('y')
            if y!=0:
                if self.guesses[t][y-1]=='X':
                    return False
            if y!=11:
                if self.guesses[t][y+1]=='X':
                    return False
        if self.dir==-1:
            return False
        return True
