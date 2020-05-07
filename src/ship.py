class Ship:
    def __init__(self, x_pos, y_pos, orientation, length, board):
        self.cells = []
        self.sunk = False
        self.set_cells(x_pos, y_pos, orientation, length, board)

    def set_cells(self, x_pos, y_pos, orientation, length, board):
        if orientation == 'V': # Vertical ship placement
            for i in range(y_pos, y_pos + length):
                cell = self.Cell(x_pos, i)
                self.cells.append(cell)
                board[i][x_pos] = 1
        elif orientation == 'H': # Horizontal ship placement
            for i in range(x_pos, x_pos + length):
                cell = self.Cell(i, y_pos)
                self.cells.append(cell)
                board[y_pos][i] = 1

    def is_ship_sunk(self):
        if self.sunk: # Ship has already been declared sunk
            return True
        elif len(self.cells) == 0: # No more cells, ship is sunk
            self.sunk = True
            return True
        else: # Ship still contains cells
            return False

    def hit(self, x_pos, y_pos):
        for i in range(0, len(self.cells)):
            if self.cells[i].x == x_pos and self.cells[i].y == y_pos:
                del self.cells[i] # On cell hit, remove from this ship's cells
                return

    class Cell: 
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return 'x pos: {}, y pos: {}'.format(self.x, self.y)
