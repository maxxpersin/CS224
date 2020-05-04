class Ship:
    def __init__(self, x_pos, y_pos, orientation, length, board):
        self.cells = []
        self.sunk = False
        self.set_cells(x_pos, y_pos, orientation, length, board)

    def set_cells(self, x_pos, y_pos, orientation, length, board):
        if orientation == 'V':
            for i in range(y_pos, y_pos + length):
                cell = self.Cell(x_pos, i)
                self.cells.append(cell)
                board[i][x_pos] = 1
        elif orientation == 'H':
            for i in range(x_pos, x_pos + length):
                cell = self.Cell(i, y_pos)
                self.cells.append(cell)
                board[y_pos][i] = 1

    def is_ship_sunk(self):
        if self.sunk:
            return True
        elif len(self.cells) == 0:
            self.sunk = True
            return True
        else:
            return False

    def hit(self, x_pos, y_pos):
        for i in range(0, len(self.cells)):
            # print(str(cell.x) + ' ' + str(cell.y))
            # print(str(x_pos) + ' ' + str(y_pos))
            if self.cells[i].x == x_pos and self.cells[i].y == y_pos:
                del self.cells[i]
                return

    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return 'x pos: {}, y pos: {}'.format(self.x, self.y)
