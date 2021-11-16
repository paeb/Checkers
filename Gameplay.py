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

    def check_piece(self,x,y, pieces): # Check if a piece is in a given position and its color
        check = False
        type = None
        for p in self._pieces:
            if (p.x == x and p.y == y):
                check = True
                type = p._color
        return check, type

    def capture(self, captured_piece):
        all_pieces = self._pieces
        if captured_piece in all_pieces:
            self.pieces = []

    def move(self,piece,direction):
        # Direction is numerical and given by [dx, dy]
        
        # Make sure that the piece can only move in the directions allowed by its color.
        # Black can move forward; white can move backward.
        if piece._color == Color.BLACK:
            assert direction[0] == 1
        if piece._color == Color.WHITE:
            assert direction[0] == -1

        [dx, dy] = direction
        [x,y] = [piece._x, piece._y]

        # Check whether there already is a piece where the current piece wishes to move.
        if self.check_piece(x + dx, y + dy, self.pieces)[0]: 
            # If the piece where you want to move is the same color as the piece to be moved
            if self.check_piece(x + dx, y + dy, self.pieces)[1] == piece._color:
                print("There is already a piece where you want to move.")
            
            # If the piece where you want to move is a different color as the piece to be moved
            elif self.check_piece(x + dx, y + dy, self.pieces)[1] != piece._color:
                # If there is a piece that's a move over from the piece that you would've jumped.
                if self.check_piece(x + 2*dx, y + 2*dy, self.pieces)[0]: 
                    print("There is already a piece where you want to move.") 
                # Move the actual piece now. 
                if not self.check_piece(x + 2*dx, y + 2*dy, self.pieces)[0]: 
                    piece._x = x + 2*dx
                    piece._y = y + 2*dy
                    # Capture the piece that was jumped. 



                # Check whether the move is in bounds or not.
                # Check whether the piece can jump multiple times.
                # If the move is not allowed, what do we return?

        return None # Change this later

board = Board()
board.show()

gameplay = Gameplay()
if __name__ == "__main__":
    gameplay.move()