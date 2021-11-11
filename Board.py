import numpy as np
from Piece import Piece
from Color import Color

class Board:

    def __init__(self):
        self._board = np.zeros((8,8))
        
        # put the white pieces on the board
        column = 1
        row = 0
        while column < 8:
            white_piece = Piece(Color.WHITE,[row,column])
            self._board[row][column] = white_piece
            column += 2

            if column >= 8 and row == 0: # out of bounds
                column = 0
                row = 1
            elif column == 8 and row == 0: # out of bounds
                column = 0
                row = 1

            