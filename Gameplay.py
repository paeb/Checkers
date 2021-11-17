from Piece import Piece
from Board import Board
from Color import Color

class Gameplay():
    def __init__(self):
        self._board = Board()
        self._pieces = self._board.get_pieces()
        self._player = 1
        self._finished = False

        self._directions = {"front right":[-1,1],
                            "front left":[-1,-1],
                            "back left":[1,1],
                            "back right":[1,-1]}

    def check_piece(self,x,y,pieces): # Check if a piece is in a given position and its color
        check = False
        type = None
        for p in pieces:
            if (p.x == x and p.y == y):
                check = True
                type = p._color
        return check, type

    # Get the piece that corresponds to a given position.
    def get_piece(self,x,y):
        p = None
        for piece in self._pieces:
            if piece._x == x and piece._y == y:
                p = piece
        return p

    def check_in_bounds(self,x,y, board_length = 8, board_width = 8): # The dimensions of the board are 8 by 8.
        return 0 <= x and x < board_length and 0 <= y and y < board_width

    def capture(self, captured_piece):
        all_pieces = self._pieces
        if captured_piece in all_pieces:
            self.pieces.remove(captured_piece) # = the pieces that are in all_piece and not captured_piece
        return None

    def move(self,piece,direction):
        # Direction is numerical and given by [dx, dy]
        
        # Make sure that the piece can only move in the directions allowed by its color.
        # Black can move forward; white can move backward.
        if piece._color == Color.BLACK:
            assert direction[0] == -1
        if piece._color == Color.WHITE:
            assert direction[0] == 1

        dx, dy = direction
        x = piece._x
        y = piece._y

        # Check whether the piece where you want to move is in bounds.
        if self.check_in_bounds(x + dx, y + dy):

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
                        if self.check_in_bounds(x + 2*dx, y + 2*dy):
                            piece._x = x + 2*dx
                            piece._y = y + 2*dy
                            # Capture the piece that was jumped. 
                            self.capture(self.get_piece(x,y))

                    # Check whether the move is in bounds or not.
                    # Check whether the piece can jump multiple times.
                    # If the move is not allowed, what do we return?

        return None # Change this later

    def play(self):
        version = 1.0
        print("--Checkers Version " + str(version) + "--")

        self._board.show()

        while not self._finished: # game is not finished
            color = None
            if self._player == 1:
                print("--Player 1 Turn--")
                color = Color.BLACK

            if self._player == 2:
                print("--Player 2 Turn--")
                color = Color.WHITE

            print("Player " + str(self._player) + "'s Turn.")
            positions = input("Which piece would you like to move? Type its coordinates (xy): ")
            piece = Piece(positions[0],positions[1],color)
            direction = input("Where would you like to move the piece? Choices: front left, front right, back right, back left: ").lower()
            numerical_direction = self._directions[direction]
            self.move(piece,numerical_direction)

if __name__ == "__main__":
    gameplay = Gameplay()
    gameplay.play()