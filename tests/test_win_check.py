import game
from pytest import mark, param


def columns_board(position, marker):
    board = [' '] * 9
    for i in range(position, 9, 3):
        board[i] = marker
    print(board)
    return board


class TestWinCheck:

    @mark.parametrize(
        "marker",
        [
            param('X', id="X marker"),
            param('Y', id="Y marker")
        ])
    def test_left_column(self, marker):
        board = columns_board(0, marker)

        assert game.win_check(board, marker)

    @mark.parametrize(
        "marker",
        [
            param('X', id="X marker"),
            param('Y', id="Y marker")
        ])
    def test_center_column(self, marker):
        board = columns_board(1, marker)

        assert game.win_check(board, marker)

    @mark.parametrize(
        "marker",
        [
            param('X', id="X marker"),
            param('Y', id="Y marker")
        ])
    def test_right_column(self, marker):
        board = columns_board(2, marker)

        assert game.win_check(board, marker)
