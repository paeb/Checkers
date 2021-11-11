from Piece import Piece



class Gameplay():
    def __init__(self, pieces):
        self.pieces = pieces

    def check_piece(x,y): # Check if a piece is in a given position
        check = False
        for p in pieces:
            if (p.x == x and p.y == y):
                check = True
        return check

    def move(self,piece,direction):
        # Direction is either forward_left, forward_right, backward_left, backward_right