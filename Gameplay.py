from Piece import Piece
from Board import Board
from Color import Color
import time

class Gameplay():
    def __init__(self):
        self._board = Board()
        self._pieces = self._board.get_pieces()
        self._player = 1
        self._finished = False

        self._directions = {"front right":[-1,1],
                            "front left":[-1,-1],
                            "back left":[1,-1],
                            "back right":[1,1]}

    def check_piece(self,x,y): # Check if a piece is in a given position and its color
        check = False
        type = None
        if self._board._board[x][y] != 0:
            check = True
            type = self._board._board[x][y]._color
        return check,type
        # check = False
        # type = None
        # for p in self._pieces:
        #     if (p._x == x and p._y == y):
        #         check = True
        #         type = p._color
        # return check, type

    # Check whether a given piece is kingable
    def check_king(self, piece):
        if piece._color == Color.WHITE:
            if piece._x == 7:
                return True
        elif piece._color == Color.BLACK:
            if piece._x == 0:
                return True
        else:
            return False

    # King all of the pieces that should be kinged.
    def king(self):
        pieces = self._pieces
        for piece in pieces:
            if self.check_king(piece):
                piece._is_king = True
        return None

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

    def can_jump(self, piece):
        x = piece._x
        y = piece._y
        if piece._color == Color.BLACK:
            dx = -1
        elif piece._color == Color.WHITE:
            dx = 1

        possible_jumps = list()

        for dy in [-1,1]:
            # Check whether the piece where you want to move is in bounds.
            if self.check_in_bounds(x + dx, y + dy):
                # Check whether there already is a piece where the current piece wishes to move.
                if self.check_piece(x + dx, y + dy)[0]:
                    # If the piece where you want to move is a different color as the piece to be moved
                    if self.check_piece(x + dx, y + dy)[1] != piece._color:
                        # If there is not a piece that's a move over from the piece that you would've jumped.
                        if not self.check_piece(x+2*dx, y+2*dy)[0]: 
                            possible_jumps.append(dy)

        if len(possible_jumps) == 2: # The player has two possible jumps
            string = input("You have two possible jumping options. Please choose left or right: ").lower()
            num_directions = {"left": -1, "right": 1}
            self.move(piece, [dx,num_directions[string]])
            return True
        elif len(possible_jumps) == 1:
            print("You have to jump over the opponent's piece. Automatically jumping...")
            time.sleep(3) # wait so that the player can see the message
            self.move(piece, [dx,possible_jumps[0]])
            return True
        else:
            return False

    def can_move(self,piece): #Check if a given piece can move
        output = False
        
        x = piece._x
        y = piece._y
        color = piece._color
        is_king = piece._is_king

        dx_list = [-1,1]
        dy_list = [-1,1]

        for dx in dx_list:
            for dy in dy_list:
                if self.check_in_bounds(x + dx, y + dy):
                    # make the output True if the piece can move. 
                    if not piece._is_king:
                        if piece._color == Color.BLACK: 
                            if dx == -1 and not self.check_piece(x+dx,y+dy)[0]:
                                output = True
                        if piece._color == Color.WHITE:
                            if dx == 1 and not self.check_piece(x+dx,y+dy)[0]:
                                output = True
        return output

    # Check if there is a winner
    def check_win(self):
        pieces = self._pieces
        black_pieces = [piece for piece in pieces if piece._color == Color.BLACK]
        white_pieces = [piece for piece in pieces if piece._color == Color.WHITE]

        # Check if each side can move or jump. If there are no pieces, then both variables will remain False.
        black_can_move = False
        white_can_move = False

        for black_piece in black_pieces:
            if self.can_move(black_piece) or self.can_jump(black_piece):
                black_can_move = True

        for white_piece in white_pieces:
            if self.can_move(white_piece) or self.can_jump(white_piece):
                white_can_move = True

        winning_color = None
        if not black_can_move:
            winning_color = Color.WHITE
        elif not white_can_move:
            winning_color = Color.BLACK

        return winning_color

        # Check if any pieces can move or jump, then check if there are any pieces at all

    def move(self,piece,direction):
        # Direction is numerical and given by [dx, dy].
        # We might have mixed up dx and dy.
        
        # Make sure that the piece can only move in the directions allowed by its color.
        # Black can move forward; white can move backward.
        if not piece._is_king:
            if piece._color == Color.BLACK:
                while direction[0] != -1:
                    direction = input("Please type a valid direction. Choices: front left, front right: ").lower()
                    direction = self._directions[direction]
            if piece._color == Color.WHITE:
                while direction[0] != 1:
                    direction = input("Please type a valid direction. Choices: back left, back right: ").lower()
                    direction = self._directions[direction]

        dx, dy = direction
        x = piece._x
        y = piece._y

        # Check whether the place where you want to move is in bounds.
        if self.check_in_bounds(x + dx, y + dy):
            # Check whether there already is a piece where the current piece wishes to move.
            if self.check_piece(x + dx, y + dy)[0]:
                # If there is a piece that's a move over from the piece that you would've jumped.
                if self.check_piece(x + 2*dx, y + 2*dy)[0]:
                    print("Can't move; there's a piece in that location.")
                else:
                    if self.check_in_bounds(x + 2*dx, y + 2*dy):
                        piece._x = x + 2*dx
                        piece._y = y + 2*dy
                        # Capture the piece that was jumped. 
                        self._board.update_pieces(x,y,2*dx,2*dy,piece,capture=True)
                    # Check whether the move is in bounds or not.
                    # Check whether the piece can jump multiple times.
                    # If the move is not allowed, what do we return?
            else:
                piece._x = x + dx
                piece._y = y + dy

                self._board.update_pieces(x,y,dx,dy,piece)
        else:
            print("Not in bounds.")

        return None # Change this later

    def play(self):
        version = 1.0
        print("--Checkers Version " + str(version) + "--")

        self._board.show()

        while not self._finished: # game is not finished
            color = None
            


            if self._player == 1:
                self.king()
                print("--Player 1 Turn--")
                color = Color.BLACK

            if self._player == 2:
                self.king()
                print("--Player 2 Turn--")
                color = Color.WHITE

            print("Player " + str(self._player) + "'s Turn.")

            jumped_piece = False

            for piece in self._board.get_pieces():
                if piece._color == color:
                    if self.can_jump(piece): # this will check if a piece can jump and jump the piece if possible
                        jumped_piece = True
                        break
                        
            if not jumped_piece: # the player can only choose their move if their piece didn't jump
                positions = input("Which piece would you like to move? Type its row,column: ").split(",")
                piece = self._board._board[int(positions[0])][int(positions[1])]
                while piece == 0 or piece._color != color:
                    positions = input("Please choose a valid piece on the board. Type its row,column: ").split(",")
                    piece = self._board._board[int(positions[0])][int(positions[1])]
                direction = input("Where would you like to move the piece? Choices: front left, front right, back right, back left: ").lower()
                numerical_direction = self._directions[direction]
                self.move(piece,numerical_direction)

            self._board.show()

            if self.check_win() != None:
            
                self._finished = True
                win_dict = {Color.BLACK: "Black", Color.WHITE: "White"}
                winner = win_dict[self.check_win()]
                print(f"--{winner} wins!--")

            if self._player == 1:
                self._player = 2
            else:
                self._player = 1

if __name__ == "__main__":
    gameplay = Gameplay()
    gameplay.play()