from Color import Color

class Piece():
    def __init__(self,x,y,color):
        self._x = int(x)
        self._y = int(y)
        self._color = color

    def __str__(self):
        if self._color == Color.BLACK:
            return 'B'
        else:
            return 'W'