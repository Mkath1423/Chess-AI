from Constants import Players

class Piece:
    name = ''

    player = ''

    has_moves = False

    move_directions = []
    move_distance = 1

    pos = [0, 0]

    def __init__(self, name, player, pos):
        self.name = name
        self.player = player
        self.pos = pos

    def __str__(self):
        return self.name

    @classmethod
    def from_string(cls, str : str, pos):
        if   str == 'p': return Pawn(Players.BLACK.value, pos)
        elif str == 'r': return Rook(Players.BLACK.value, pos)
        elif str == 'n': return Knight(Players.BLACK.value, pos)
        elif str == 'b': return Bishop(Players.BLACK.value, pos)
        elif str == 'q': return Queen(Players.BLACK.value, pos)
        elif str == 'k': return King(Players.BLACK.value, pos)

        elif str == 'P': return Pawn(Players.WHITE.value, pos)
        elif str == 'R': return Rook(Players.WHITE.value, pos)
        elif str == 'N': return Knight(Players.WHITE.value, pos)
        elif str == 'B': return Bishop(Players.WHITE.value, pos)
        elif str == 'Q': return Queen(Players.WHITE.value, pos)
        elif str == 'K': return King(Players.WHITE.value, pos)
        else           : return None

class Bishop(Piece):
    def __init__(self, player, pos):
        super(Bishop, self).__init__('b'  if player == Players.BLACK.value else 'B', player, pos)

        self.move_directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.move_distance = 8

class Rook(Piece):
    def __init__(self, player, pos):
        super(Rook, self).__init__('r' if player == Players.BLACK.value else 'R', player, pos)

        self.move_directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        self.move_distance = 8

class Queen(Piece):
    def __init__(self, player, pos):
        super(Queen, self).__init__('q' if player == Players.BLACK.value else 'Q', player,pos)

        self.move_directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]
        self.move_distance = 8

class King(Piece):
    def __init__(self, player, pos):
        super(King, self).__init__('k' if player == Players.BLACK.value else 'K', player, pos)

        self.move_directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]
        self.move_distance = 1

class Knight(Piece):
    def __init__(self, player, pos):
        super(Knight, self).__init__('n' if player == Players.BLACK.value else 'N', player, pos)

        self.move_directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        self.move_distance = 1

class Pawn(Piece):
    def __init__(self, player, pos):
        super(Pawn, self).__init__('p' if player == Players.BLACK.value else 'P', player, pos)

        self.move_directions = [(1 if player == Players.WHITE.value else -1 , 0)]
        self.move_distance = 1
