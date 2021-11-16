from Piece import Piece
from Board import Board
from Color import Color

class Gameplay():
    def __init__(self, pieces):
        self._pieces = pieces
        self._board = Board()
        self._player = 1
        self._finished = False

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
            if self.check_piece(x + dx, y + dy, self.pieces)[1] == piece._color:
                pass
        return None # Change this later

    def play(self):
        version = 1.0
        print("--Checkers Version " + str(version) + "--")

        self._board.show()

        while not self._finished:
            if self._player == 1:
                print("--Player 1 Turn--:")
                positions = input("Which piece would you like to move? Please input coordinates")
                piece = Piece(positions[0],positions[1],Color.BLACK)
                direction = input("Where would you like to move the piece?")
                self.move(piece,direction)
            if self._player == 2:
                pass

gameplay = Gameplay()
if __name__ == "__main__":
    gameplay.move()