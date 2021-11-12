import pygame
from damka_assets import *
from damka_assets.piece_class import Piece, SmallPiece
from damka_assets.functions import opposite_color
from AI import get_all_moves, shuffle, make_temp_move
pygame.init()


class Board:

    def __init__(self):
        self.board = []
        # keep track of pieces:
        self.red_left = self.white_left = 12
        self.red_queens = self.white_queens = 0
        # create the Board
        self.create_pieces()
        self.is_error_msg_visible = False
        self.is_win_msg_visible = False
        self.is_game_over = False

    def toggle_error_visibility(self):
        self.is_error_msg_visible = not self.is_error_msg_visible

    def toggle_game_over_msg(self):
        self.is_win_msg_visible = not self.is_win_msg_visible

    def create_pieces(self):
        # placing the pieces on the board
        for row in range(ROWS):
            # initializing each rows pieces
            self.board.append([])
            for col in range(COLS):
                # selecting on which square to draw a piece
                if col % 2 == ((row + 1) % 2):
                    # white = top 3 rows
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    # red = bottom 3 rows
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))

                    else:
                        self.board[row].append(0)
                    # blank squares will be equal to 0
                else:
                    self.board[row].append(0)

    def get_piece_at(self, row, col):
        return self.board[row][col]

    def move_piece(self, piece, row, col):
        # move the piece within the board.
        # remove the old piece and create a new one at [row, col]
        # here we swap the positions:
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # is it a queen now?
        # we make sure it isn't a queen already.
        if row == ROWS - 1 or row == 0:
            if not piece.queen:
                piece.make_queen()
                if piece.color == RED:
                    self.red_queens += 1
                else:
                    self.white_queens += 1

    def remove_piece(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if type(piece) != int:
                if piece.color == WHITE:
                    self.white_left -= 1
                else:
                    self.red_left -= 1

    def show_quit_msg(self):
        pygame.draw.rect(WIN, BLACK, ((100, 200), (600, 300)))
        large_font = pygame.font.SysFont('Arial', 50)
        small_font = pygame.font.SysFont('Arial', 40)

        msg = large_font.render('Are you sure you want to quit?', True, HAKI)
        yes = small_font.render('Yes', True, RED)
        no = small_font.render('No', True, RED)

        pygame.draw.rect(WIN, WHITE, ((205, 370), (100, 70)))  # yes
        pygame.draw.rect(WIN, WHITE, ((495, 370), (100, 70)))  # no

        WIN.blit(msg, (125, 250))
        WIN.blit(yes, (225, 380))
        WIN.blit(no, (525, 380))

    def draw_squares(self, window):
        # drawing the squares
        window.fill(HAKI)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                # start from 0 or 1, then jump by 2
                # that's because the order is haki-brown-haki-brown
                pygame.draw.rect(window, BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.queen:
            moves.update(self.search_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.search_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.queen:
            moves.update(self.search_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self.search_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    def search_left(self, start, stop, step, color, left, skipped_pieces=[]):
        # start & stop = row num
        # step = which direction (up / down the board)
        # left = which column
        moves = {}
        last_seen = []
        for r in range(start, stop, step):
            if left < 0:  # outside the board
                break

            current_square = self.board[r][left]

            if current_square == 0:  # empty square
                if skipped_pieces and not last_seen:  # we skipped a piece, and had not seen one yet
                    break
                elif skipped_pieces:  # double jump check
                    moves[(r, left)] = last_seen + skipped_pieces
                else:
                    # add as a valid move
                    moves[(r, left)] = last_seen

                if last_seen:
                    # we skipped over a piece
                    # here we check double jumps
                    if step == -1:  # which direction
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self.search_left(r + step, row, step, color, left - 1, skipped_pieces=last_seen))
                    moves.update(self.search_right(r + step, row, step, color, left + 1, skipped_pieces=last_seen))
                break

            elif current_square.color == color:
                # we can't move to a same colored piece square
                break
            else:
                # opposite color, we'll save it to "last"
                last_seen = [current_square]

            left -= 1

        return moves

    def search_right(self, start, stop, step, color, right, skipped_pieces=[]):
        # start & stop = row num
        # step = which direction (up / down the board)
        # left = which column
        moves = {}
        last_seen = []
        for r in range(start, stop, step):
            if right >= COLS:  # outside the board
                break

            current_square = self.board[r][right]

            if current_square == 0:  # empty square
                if skipped_pieces and not last_seen:  # we skipped a piece, and had not seen one yet
                    break
                elif skipped_pieces:  # double jump check
                    moves[(r, right)] = last_seen + skipped_pieces
                else:
                    # add as a valid move
                    moves[(r, right)] = last_seen

                if last_seen:
                    # we skipped over a piece
                    # here we check double jumps
                    if step == -1:  # which direction
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self.search_left(r + step, row, step, color, right - 1, skipped_pieces=last_seen))
                    moves.update(self.search_right(r + step, row, step, color, right + 1, skipped_pieces=last_seen))
                break

            elif current_square.color == color:
                # we can't move to a same colored piece square
                break
            else:
                # opposite color, well save it to "last"
                last_seen = [current_square]

            right += 1

        return moves

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def evaluate(self):
        # white is the AI, maximizing too

        return self.white_left - self.red_left + (self.white_queens * 0.5 - self.red_queens * 0.5)

    def draw(self, window, arrows_info=None):
        # drawing everything - squares and pieces
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                # don't draw empty squares
                if piece != 0:
                    piece.draw(window)

        # the quit button

        window.blit(quit_button, (0, 0))
        if self.is_error_msg_visible:
            self.show_quit_msg()

        # game over message
        if self.is_win_msg_visible:
            window.blit(game_over_img, (0, 218))

        # back show
        if not self.is_win_msg_visible and self.check_win():
            window.blit(back_show_img, (5, 225))

        # arrows
        if arrows_info:
            for arrow in arrows_info:
                window.blit(arrow[0], arrow[1])

    def check_win(self):
        if self.white_left == 0:
            return RED
        if self.red_left == 0:
            return WHITE

        white_has_moves = False
        for white_piece in self.get_all_pieces(WHITE):
            moves = self.get_valid_moves(white_piece)
            if len(moves) > 0:
                white_has_moves = True
                break

        red_has_moves = False
        for red_piece in self.get_all_pieces(RED):
            moves = self.get_valid_moves(red_piece)
            if len(moves) > 0:
                red_has_moves = True
                break

        if not white_has_moves:
            return RED
        if not red_has_moves:
            return WHITE

        # draw
        if self.red_queens == self.white_queens == 1 and self.red_left == self.white_left == 0:
            return WHITE

        return None


class SmallBoard(Board):

    def create_pieces(self):
        # placing the pieces on the board
        for row in range(ROWS):
            # initializing each rows pieces
            self.board.append([])
            for col in range(COLS):
                # selecting on which square to draw a piece
                if col % 2 == ((row + 1) % 2):
                    # white = top 3 rows
                    if row < 3:
                        self.board[row].append(SmallPiece(row, col, WHITE))
                    # red = bottom 3 rows
                    elif row > 4:
                        self.board[row].append(SmallPiece(row, col, RED))

                    else:
                        self.board[row].append(0)
                    # blank squares will be equal to 0
                else:
                    self.board[row].append(0)

    def draw_squares(self, window):
        # drawing the squares
        # window.fill(HAKI)
        # haki first row:
        for x in range(1, 8, 2):
            pygame.draw.rect(window, HAKI, (x*80, 0, SMALL_SQUARE_SIZE, SMALL_SQUARE_SIZE))

        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                # start from 0 or 1, then jump by 2
                # that's because the order is haki-brown-haki-brown
                pygame.draw.rect(window, BROWN, (row * SMALL_SQUARE_SIZE, col * SMALL_SQUARE_SIZE, SMALL_SQUARE_SIZE, SMALL_SQUARE_SIZE))


        for row in range(ROWS):
            for col in range(row % 2 + 1, ROWS, 2):
                # start from 0 or 1, then jump by 2
                # that's because the order is haki-brown-haki-brown
                pygame.draw.rect(window, HAKI, (row * SMALL_SQUARE_SIZE, col * SMALL_SQUARE_SIZE, SMALL_SQUARE_SIZE, SMALL_SQUARE_SIZE))


    def draw(self, window, arrows_info=None):
        # drawing everything - squares and pieces
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                # don't draw empty squares
                if piece != 0:
                    piece.draw(window)

        # arrows
        if arrows_info:
            for arrow in arrows_info:
                window.blit(arrow[0], arrow[1])


def compare_boards(b1, b2):
    for row in range(8):
        for col in range(8):
            b1_square, b2_square = b1[row][col], b2[row][col]
            # piece != 0
            if type(b1_square) != type(b2_square):
                return False
            # if pieces, check the attributes
            if isinstance(b1_square, Piece):
                if b1_square.color != b2_square.color:
                    return False
                if b1_square.queen != b2_square.queen:
                    return False
            # if zeros
            elif b1_square != b2_square:
                return False
    return True


