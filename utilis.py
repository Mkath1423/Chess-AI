def uci_to_index(squares):
    if isinstance(squares, str):
        assert (len(squares) == 2), ValueError("square must be 2 charaters long. (A1)")

        return int(squares[1]) - 1, 'abcdefgh'.index(squares[0].lower())

    elif isinstance(squares, list):
        assert all([len(square) == 2 for square in squares]), ValueError("square must be 2 charaters long. (A1)")

        return [(int(square[1]) - 1, 'abcdefgh'.index(square[0].lower())) for square in squares]

def index_to_uci(squares: tuple):
    if isinstance(squares, tuple):
        assert (len(squares) == 2), ValueError(f"square must be 2 charaters long. {len(squares)}")

        return 'abcdefgh'[squares[0]] + str(squares[1] + 1)

    elif isinstance(squares, list):
        assert all([(len(square) == 2) for square in squares]), ValueError("square must be 2 charaters long. (A1)")

        return ['abcdefgh'[square[0]] + str(square[1] + 1) for square in squares]


