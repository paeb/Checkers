from Piece import Piece
from Board import Board

class Gameplay():
    def __init__(self, pieces):
        self.pieces = pieces

    def check_piece(self,x,y): # Check if a piece is in a given position
        check = False
        for p in self.pieces:
            if (p.x == x and p.y == y):
                check = True
        return check

    def move(self,piece,direction):
        pass
        # Direction is either forward_left, forward_right, backward_left, backward_right

board = Board()
board.show()