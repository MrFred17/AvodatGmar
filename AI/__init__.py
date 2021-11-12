from copy import deepcopy
from damka_assets import RED, WHITE
import random


class SearchTree:

    def __init__(self, depth, player_color):
        self.depth = depth
        self.player_color = player_color

    def find_optimal_move(self, board):
        is_max = True
        if self.player_color == RED:
            is_max = False
        return self._minimax_alpha_beta(0, board, is_max, float('-inf'), float('inf'))[1]

    def _minimax_alpha_beta(self, current_depth, board, is_max_turn, alpha, beta):
        if is_max_turn:
            self.player_color = WHITE
        else:
            self.player_color = RED

        if current_depth == self.depth or board.check_win():
            return board.evaluate(), board

        best_value = float('-inf') if is_max_turn else float('inf')
        best_move = None
        for move in get_all_moves(board, self.player_color):

            value, _ = self._minimax_alpha_beta(current_depth + 1, move, not is_max_turn, alpha, beta)

            if is_max_turn and best_value < value:
                best_value = value
                best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break

            elif (not is_max_turn) and best_value > value:
                best_value = value
                best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break

        return best_value, best_move


def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece_at(piece.row, piece.col)
            new_board = make_temp_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return shuffle(moves)


def make_temp_move(piece, move, board, skipped):
    board.move_piece(piece, move[0], move[1])
    if skipped:
        board.remove_piece(skipped)
    return board


def shuffle(lst):
    for i in range(len(lst)):
        r1 = random.randint(0, len(lst) - 1)
        r2 = random.randint(0, len(lst) - 1)
        lst[r1], lst[r2] = lst[r2], lst[r1]
    return lst








