from utilis import *
from pieces import Piece

# class board:
    # stores the current position
    # stores castling rights
    # stores who to play
    # stores the move count

    # stores the previous board (of this type)

    # class method
    # make move (board, uci)
    # return new board with updated position

class Board:
    start_position = [['' for j in range(8)] for i in range(8)]

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

    @classmethod
    def fromfen(cls, fen: str):
        b = cls()
        b.start_position = cls.fen_to_array(fen)
        b.current_position = cls.fen_to_array(fen)

        return b

    def __str__(self):
        output = '  A B C D E F G H \n'
        for i, rank in enumerate(self.current_position):
            output += f'{i + 1} '
            for square in rank:
                if square == '':
                    output += '.'

                else:
                    output += str(square)

                output += ' '

            output += '\n'

        return "\n".join(output.split('\n')[::-1])


    @classmethod
    def fen_to_array(self, fen):
        board_position = [['' for i in range(8)] for j in range(8)]
        current_rank = 0
        current_file = 0
        for char in fen:
            if char == '/':
                current_rank += 1
                current_file = 0

            elif char.isdigit():
                current_file += int(char)

            else:
                board_position[current_rank][current_file] = Piece.from_string(char, (current_rank, current_file))
                current_file += 1

        return board_position[::-1]

    # assert all([coord < 8 and coord > 0 for square in squares for coord in square]), ValueError(
    #    "Coordinates out of range.")

    def move_piece_uci(self, move: list):
        start_index = uci_to_index(move[:2])
        end_index = uci_to_index(move[2:])

        temp = self.current_position[start_index[0]][start_index[1]]
        self.current_position[start_index[0]][start_index[1]] = self.current_position[end_index[0]][end_index[1]]
        self.current_position[end_index[0]][end_index[1]] = temp

        self.moves.append(move)

    def find_moves(self, piece : Piece):
        valid_moves = []

        for direction in piece.move_directions:
            for distance in range(1, piece.move_distance + 1):
                position_to_check = [piece.current_position[0] + direction[0]*distance,piece.current_position[1] + direction[1]*distance]

                if position_to_check[0] > 7 or position_to_check[0] < 0 or position_to_check[1] > 7 or position_to_check[1] < 0:
                    break

                if self.current_position[position_to_check[0]][position_to_check[1]] == '':
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

