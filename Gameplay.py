from Piece import Piece
from Board import Board
from Color import Color

# Define a dictionary for the four directions in which a piece can move. 
'''
directions = {["forward","left"]:[-1,1],
                ["forward","right"]:[1,1],
                ["backward","left"]:[-1,-1],
                ["backward","right"]:[1,-1]
                }
'''

directions = dict()

class Gameplay():
    def __init__(self, pieces):
        self._pieces = pieces

    def check_piece(x,y, pieces): # Check if a piece is in a given position
        check = False
        for p in pieces:
            if (p.x == x and p.y == y):
                check = True
        return check

    def move(self,piece,direction):
        # Direction is either ["forward","left"], ["forward","right"], ["backward","left"], or ["backward","right"]
        
        # Make sure that the piece can only move in the directions allowed by its color.
        # Black can move forward; white can move backward.
        if piece._color == Color.BLACK:
            assert direction[0] == "forward"
        if piece._color == Color.WHITE:
            assert direction[0] == "backward"

        # Represent the change in position numerically based on the string input of direction.
        [dx, dy] = directions[direction]
        [x,y] = [piece._x, piece._y]
        self.check_piece(x + dx, y + dy, self._pieces)

board = Board()
board.show()
        
