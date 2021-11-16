from Piece import Piece
from Board import Board
from Color import Color

class Gameplay():
    def __init__(self, pieces):
        self._pieces = pieces
        self._directions = {"fr":[-1,1],
                            "fl":[-1,-1],
                            "br":[1,1],
                            "bl":[1,-1]}

    def check_piece(self,x,y): # Check if a piece is in a given position and its color
        check = False
        type = None
        for p in self._pieces:
            if (p.x == x and p.y == y):
                check = True
                type = p._color
        return check, type

    def move(self,piece,direction):
        # Direction is numerical and given by [dx, dy]
        
        # Make sure that the piece can only move in the directions allowed by its color.
        # Black can move forward; white can move backward.
        if piece._color == Color.BLACK:
            assert direction[0] == "forward"
        if piece._color == Color.WHITE:
            assert direction[0] == "backward"

        [dx, dy] = direction
        [x,y] = [piece._x, piece._y]
        self.check_piece(x + dx, y + dy, self._pieces)

        # Check whether there already is a piece where the current piece wishes to move.
        if self.check_piece(x + dx, y + dy, self.pieces)[0]: 
            print("cannot move there!")
        else:
            self._pieces[x + dx, y + dy] = piece

        return None # Change this later

board = Board()
board.show()

gameplay = Gameplay()
if __name__ == "__main__":
    gameplay.move()