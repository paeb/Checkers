from enum import Enum

class Color(Enum):
    black = 0
    white = 1

class Piece():
    def __init__(self,position,color):
        self._position = position
        self._color = color