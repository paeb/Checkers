from enum import Enum

class Color(Enum):
    black = 0
    white = 1

class Piece():
    def __init__(self,x,y,color):
        self._x = x
        self._y = y
        self._color = color

