from damka_assets.game_class import *


class Puzzle:
    def __init__(self, window, board, turn, correct_board, first_move):
        self.window = window
        self.original_board = board
        self.original_turn = turn
        self.game = SmallGame(self.window, correct_board=correct_board)
        self.game.board.board = board
        self.game.turn = turn
        self.correct_board = correct_board
        self.first_move = first_move

    def try_again(self):
        # user clicks "try again" button
        self.game.board.board = self.original_board
        self.game.turn = self.original_turn




