# Main
#
# Battle-Py!
#
# Authors: Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin
#
#

from tkinter import *
from player import Player


def place_ship(x_loc, y_loc):
    print('{} {}'.format(x_loc, y_loc))
    bname = board1[x_loc][y_loc]
    print(bname)


def create_board(root, board):
    arr = [0] * 12
    for i in range(0, 12):
        arr[i] = [0] * 12
        for j in range(0, 12):
            if board == 1:
                b = Button(root, text='?')
            elif board == 2:
                b = Button(root, text='x', command=lambda : place_ship(i, j))
            #b = Button(root, text='{}, {}'.format(i, j))
            b.grid(row=j, column=i)
            arr[i][j] = b

    return arr


main_board = Tk()
main_board.grid()
main_board.winfo_toplevel().title('Main')

guess_board = Tk()
guess_board.grid()
guess_board.winfo_toplevel().title('Guesses')

board1 = create_board(main_board, 1)
board2 = create_board(guess_board, 2)

main_board.mainloop()
guess_board.mainloop()