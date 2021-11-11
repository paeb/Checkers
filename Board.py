import numpy as np
from Piece import Piece
from Color import Color

class Board:

    def __init__(self):
        
        self._board = list()

        for i in range(0,8): # 2D list
            row = []
            for j in range(0,8):
                row.append(0)
            self._board.append(row)
        
        # put the white pieces on the board
        column = 1
        row = 0
        while column < 8:
            white_piece = Piece(row,column,Color.WHITE)
            self._board[row][column] = white_piece
            column += 2

            if column >= 8 and row == 0: # out of bounds
                column = 0
                row = 1
            elif column >= 8 and row == 1: # out of bounds
                column = 1
                row = 2

        # put the black pieces on the board
        column = 0
        row = 5
        while column < 8:
            black_piece = Piece(row,column,Color.BLACK)
            self._board[row][column] = black_piece
            column += 2

            if column >= 8 and row == 5: # out of bounds
                column = 1
                row = 6
            elif column >= 8 and row == 6: # out of bounds
                column = 0
                row = 7

    def show(self):
        for row in self._board:
            for val in row:
                print(val,end=' | ')
            print('')