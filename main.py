import Constants
from board import Board
from pieces import *
from utilis import *

def main():

    b = Board.fromfen(Constants.Positions.DEFAULT.value)
    print(b.current_position)


    # start_pos = tuple(uci_to_index('a3'))
    # b.current_position[start_pos[0]][start_pos[1]] = 'q'
    #
    # p = Queen(Constants.Players.WHITE.value)
    # p.current_position = start_pos
    # possible_moves = p.find_moves(b)
    #
    # for location in possible_moves:
    #     b.current_position[location[0]][location[1]] = 'o'
    #
    # print(b)


if __name__ == '__main__':
    main()
