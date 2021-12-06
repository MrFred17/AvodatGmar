import pygame
from damka_assets.functions import *
from damka_assets.board_class import *


class Game:
    def __init__(self, window, ai_diff=None, user_id=None, correct_board=None):
        self.window = window
        self.new_board()
        self.started = False
        self.correct_board = correct_board
        self.stats = None
        self.started_puzzle = True
        if user_id:
            self.stats = GameStats(ai_diff, user_id)

    def update_game(self, arrows=None):
        self.board.draw(self.window, arrows)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select_piece(self, row, col):
        if not self.board.is_game_over and self.started_puzzle and not self.board.is_draw_offer_visible and not self.board.is_draw:
            # selection based on mouse click position
            if self.selected:  # if we selected SOMETHING
                result = self.make_move(row, col)  # let's try to move it to pressed [row, col]

                if result is False:  # if we didn't end up moving
                    self.selected = None  # reset selection
                    self.select_piece(row, col)  # reset [row, col] to take new values

            # when a piece is selected:
            if row > 7 or col > 7:
                return False
            piece = self.board.get_piece_at(row, col)

            # is there actually a piece there?
            # is it the right piece's color turn?
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True  # selection was valid

            return False  # selection was invalid

    def switch_turns(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = RED
        else:
            self.turn = WHITE
        if self.stats:
            self.stats.total_moves += 1

    def make_move(self, row, col):
        # after we already selected
        # params: (row, col) => location to move to
        if not self.board.is_game_over:
            selected_piece = self.board.get_piece_at(row, col)
            if (row, col) in self.valid_moves and self.selected and selected_piece == 0:
                # 1) it's a valid move | 2) we selected something | 3) we selected an empty square to move to
                self.board.move_piece(self.selected, row, col)

                # start the timer for stats
                if self.stats:
                    if not self.started:
                        self.stats.start_timer()
                        self.started = True

                skipped_piece = self.valid_moves[(row, col)]
                if skipped_piece:
                    self.board.remove_piece(skipped_piece)
                self.switch_turns()

                return True

            return False

    def new_board(self):
        self.board = Board()
        self.turn = RED
        self.selected = None
        self.valid_moves = {}

    def draw_valid_moves(self, moves):
        if not self.board.is_win_msg_visible and not self.board.is_game_over:
            for move in moves:
                row, col = move
                pygame.draw.circle(self.window, BLUE,
                                   (col * SQUARE_SIZE + SQUARE_MIDDLE, row * SQUARE_SIZE + SQUARE_MIDDLE), 15)

    def reset_game(self, ai_depth, user_id):
        self.new_board()
        if user_id:
            self.stats = GameStats(ai_depth, user_id)
            self.started = False

    def ai_move(self, board):
        # doesn't return which piece to move, just a board
        # the game will update to that board
        self.board = board
        self.switch_turns()


class SmallGame(Game):

    def new_board(self):
        self.board = SmallBoard()
        self.turn = RED
        self.selected = None
        self.valid_moves = {}

    def draw_valid_moves(self, moves):
        if not self.board.is_win_msg_visible:
            for move in moves:
                row, col = move
                pygame.draw.circle(self.window, BLUE,
                                   (col * SMALL_SQUARE_SIZE + SMALL_SQUARE_MIDDLE, row * SMALL_SQUARE_SIZE + SMALL_SQUARE_MIDDLE), 15)

    def check_move(self):
        self.board.is_game_over = True
        return compare_boards(self.board.board, self.correct_board)

    def make_move(self, row, col):
        if not self.board.is_game_over:
            moved = super().make_move(row, col)
            if moved:
                self.check_move()





