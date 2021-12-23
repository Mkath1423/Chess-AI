from utilis import *
from pieces import Piece

class Board:
    start_position = ''

    current_position = [['' for j in range(8)] for i in range(8)]

    whiteToMove = True

    whiteCanCastleShort = True
    whiteCanCastleLong  = True
    blackCanCastleShort = True
    blackCanCastleLong  = True

    n_moves = 0

    moves = []

    def __init__(self):
        pass

    def __getitem__(self, index):
        if isinstance(index, str):
            index = (index[0], int(index[1]))
        if isinstance(index, int): raise ValueError('Index must be tuple or str')
        elif isinstance(index, tuple):
            if isinstance(index[0], str):
                return self.current_position[index[1] - 1]['ABCDEFGH'.index(index[0].upper())]
            else:
                return self.current_position[index[1] - 1][index[0] - 1]

    @classmethod
    def fromfen(cls, fen: str):
        b = cls()
        b.start_position = fen
        b.current_position = cls.fen_to_array(fen)
        return b

    def __str__(self):
        output = '  A B C D E F G H '
        for i, rank in enumerate(self.current_position):
            output += f'\n{i+1} '
            for square in rank:
                if square == '':
                    output += '.'

                else:
                    output += str(square)

                output += ' '

        out = output.split('\n')
        if self.whiteToMove:
            out = [out[0]] + out[-1:0:-1]

        return "\n".join(out)

        # remember me :( --> return "\n".join(output.split('\n')[::-1 if self.whiteToMove else 1])

    @classmethod
    def fen_to_array(cls, fen):
        board_position = [['' for _ in range(8)] for _ in range(8)]
        current_rank = 7
        current_file = 0

        for char in fen:
            if char == '/':
                current_rank -= 1
                current_file = 0

            elif char.isdigit():
                current_file += int(char)

            else:
                board_position[current_rank][current_file] = Piece.from_string(char, (current_file + 1, current_rank + 1))
                current_file += 1

        return board_position

    # assert all([coord < 8 and coord > 0 for square in squares for coord in square]), ValueError(
    #    "Coordinates out of range.")

    def move_piece_uci(self, move: list):
        start_index = uci_to_index(move[:2])
        end_index = uci_to_index(move[2:])

        temp = self.current_position[start_index[0]][start_index[1]]
        self.current_position[start_index[0]][start_index[1]] = self.current_position[end_index[0]][end_index[1]]
        self.current_position[end_index[0]][end_index[1]] = temp

        self.moves.append(move)

    def find_moves(self, piece: Piece):
        if isinstance(piece, str):
            return []
        valid_moves = []

        for direction in piece.move_directions:

            for distance in range(1, piece.move_distance + 1):
                position_to_check = [piece.pos[0] + direction[0]*distance, piece.pos[1] + direction[1]*distance]

                if not (position_to_check[0] in range(1, 9) and position_to_check[1] in range(1, 9)):
                    break

                if self[position_to_check[0], position_to_check[1]] == '':
                    valid_moves.append(position_to_check)
                else:
                    break

        return valid_moves

    def generate_fen(self):
        output = ''
        for rank in self.current_position:
            for square in rank:
                if square != '':
                    output += square
                elif output[-1].isdigit():
                    output = output[:-1] + str(int(output[-1]) + 1)
                else:
                    output += '1'
            output += '/'

        return output[:-1]