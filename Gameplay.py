from Piece import Piece
<<<<<<< HEAD

# Define a dictionary for the four directions in which a piece can move. 
directions = {["forward","left"]:[-1,1],
                ["forward","right"]:[1,1],
                ["backward","left"]:[-1,-1],
                ["backward","right"]:[1,-1]
                }
=======
from Board import Board
>>>>>>> 597469d42d46d2f96435a21f9ebe1ca6ce6a70cc

class Gameplay():
    def __init__(self, pieces):
        self.pieces = pieces

<<<<<<< HEAD
    def check_piece(x,y, pieces): # Check if a piece is in a given position
=======
    def check_piece(self,x,y): # Check if a piece is in a given position
>>>>>>> 597469d42d46d2f96435a21f9ebe1ca6ce6a70cc
        check = False
        for p in self.pieces:
            if (p.x == x and p.y == y):
                check = True
        return check

    def move(self,piece,direction):
<<<<<<< HEAD
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
        check_piece(x + dx, y + dy, self.pieces)
        
=======
        pass
        # Direction is either forward_left, forward_right, backward_left, backward_right

board = Board()
board.show()
>>>>>>> 597469d42d46d2f96435a21f9ebe1ca6ce6a70cc
