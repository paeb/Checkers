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

    def get_pieces(self):
        self._pieces = list()

        for i in range(8):
            for j in range(8):
                piece = self._board[i][j]
                if type(piece) == Piece:
                    self._pieces.append(piece)

        return self._pieces

    def show(self):

        print(' ___ ___ ___ ___ ___ ___ ___ ___')
        for i in range(8): # each row
            for j in range(8): # each column
                val = self._board[i][j]
                if val == 0:
                    val = ' '

                ending = '_|_'
                if j == 0:
                    print('|_',end='')
                elif j == 7:
                    ending = '_| ' + str(i)
                
                print(str(val) + '\u0332',end=ending)
            print() # new line
        print("  0   1   2   3   4   5   6   7  ")