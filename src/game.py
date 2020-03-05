# Main 
# 
# Battle-Py!
#
# Authors: Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin
#
#

from tkinter import *
from player import Player


def create_board(root):
    arr = [0] * 12
    for i in range(0, 12):
        arr[i] = [0] * 12
        for j in range(0, 12):
            b = Button(root, text='{}, {}'.format(i, j))
            b.grid(row=j, column=i)
            arr[i][j] = b

    return arr


root = Tk()
root.grid()

board1 = create_board(root)
board2 = create_board(root)

root.mainloop()

# Ship_num = 5

# grid= []
# for i in range(10):
#     grid.append(['0','0','0','0','0','0','0','0','0','0'])
# grid[3][4]=1
# print grid
