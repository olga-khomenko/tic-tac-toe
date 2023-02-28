import game
from pytest import mark, param


class TestWinCheck:

    @mark.parametrize(
        "marker, position",
        [
            param('X', 0, id="X marker at 0 position"),
            param('Y', 0, id="Y marker at 0 position"),
            param('X', 1, id="X marker at 1 position"),
            param('Y', 1, id="Y marker at 1 position"),
            param('X', 2, id="X marker at 2 position"),
            param('Y', 2, id="Y marker at 2 position")
        ])
    def test_columns(self, marker, position):
        board = [' '] * 9
        for i in range(position, 9, 3):
            board[i] = marker
        print(board)

        assert game.win_check(board, marker)

    @mark.parametrize(
        "marker, position",
        [
            param('X', 0, id="X marker at 0 position"),
            param('Y', 0, id="Y marker at 0 position"),
            param('X', 3, id="X marker at 1 position"),
            param('Y', 3, id="Y marker at 1 position"),
            param('X', 6, id="X marker at 2 position"),
            param('Y', 6, id="Y marker at 2 position")
        ])
    def test_rows(self, marker, position):
        board = [' '] * 9
        for i in range(position, position + 3):
            board[i] = marker
        print(board)

        assert game.win_check(board, marker)

    @mark.parametrize(
        "marker, positions",
        [
            param("X", [2, 4, 6], id="X diagonal right to left"),
            param("X", [0, 4, 8], id="X diagonal left to right"),
            param("Y", [2, 4, 6], id="Y diagonal right to left"),
            param("Y", [0, 4, 8], id="Y diagonal left to right"),
        ])
    def test_diagonals(self, marker, positions):
        board = [' '] * 9
        for position in positions:
            board[position] = marker
        print(board)

        assert game.win_check(board, marker)
