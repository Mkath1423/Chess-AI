import Constants
from board import Board
from pieces import *
from utilis import *

def main():
    b = Board.fromfen('Q7/8/8/8/8/8/8/B6p')
    print(b)

    moves = b.find_moves(b['a8'])

    grid = [['.' for i in range(8)] for _ in range(8)]

    for move in moves:
        grid[move[1] - 1][move[0] - 1] = 'o'

    print('  A B C D E F G H')
    for i, row in enumerate(grid[::-1]):
        print(f'{i} ', end='')
        for col in row:
            print(f'{col} ', end="")
        print('')

    print(moves)

if __name__ == '__main__':
    main()
