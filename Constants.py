from enum import Enum

class Pieces(Enum):
    WHITE_ROOK = 'R'
    WHITE_KNIGHT = 'N'
    WHITE_BISHOP = 'B'
    WHITE_QUEEN = 'Q'
    WHITE_KING = 'K'
    WHITE_PAWN = 'P'

    BLACK_ROOK = 'r'
    BLACK_KNIGHT = 'n'
    BLACK_BISHOP = 'b'
    BLACK_QUEEN = 'q'
    BLACK_KING = 'k'
    BLACK_PAWN = 'p'

class Players(Enum):
    WHITE = 'w'
    BLACK = 'b'

class Positions(Enum):
    DEFAULT = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    NONE = '8/8/8/8/8/8/8/8'

class Communications(Enum):
    RED_VALUE = '1'
    GREEN_VALUE = '2'
    BLUE_VALUE = '3'

    RANKS = 2
    FILES = 5
