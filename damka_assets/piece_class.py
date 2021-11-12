import pygame
from damka_assets import *

pygame.init()


class Piece:
    PADDING = 15
    OUTLINE = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.queen = False
        self.x = 0
        self.y = 0
        self.calculate_pos()

    def __repr__(self):
        return str(self.color)

    def calculate_pos(self):
        # calculate (x,y) values based on current row & col
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def move(self, row, col):
        # moving to piece to board[row, col]
        self.row = row
        self.col = col
        self.calculate_pos()

    def make_queen(self):
        # turn the piece into a queen
        self.queen = True

    def draw(self, window):
        # draw the piece itself
        radius = SQUARE_MIDDLE - self.PADDING
        pygame.draw.circle(window, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        # check if queen
        if self.queen:
            if self.color == WHITE:
                window.blit(BLACK_QUEEN, (self.x - QUEEN_WIDTH // 2, self.y - QUEEN_HEIGHT // 2))
            else:
                window.blit(WHITE_QUEEN, (self.x - QUEEN_WIDTH // 2, self.y - QUEEN_HEIGHT // 2))

    def compare_piece(self, other):
        a = self.row == other.row and self.col == other.col
        b = self.color == other.color and self.queen is other.queen
        return a and b


class SmallPiece(Piece):
    PADDING = 10
    OUTLINE = 2

    def calculate_pos(self):
        # calculate (x,y) values based on current row & col
        self.x = SMALL_SQUARE_SIZE * self.col + SMALL_SQUARE_SIZE // 2
        self.y = SMALL_SQUARE_SIZE * self.row + SMALL_SQUARE_SIZE // 2

    def draw(self, window):
        # draw the piece itself
        radius = SMALL_SQUARE_MIDDLE - self.PADDING
        pygame.draw.circle(window, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        # check if queen
        if self.queen:
            if self.color == WHITE:
                window.blit(SMALL_BLACK_QUEEN, (self.x - SMALL_QUEEN_WIDTH // 2, self.y - SMALL_QUEEN_HEIGHT // 2))
            else:
                window.blit(SMALL_WHITE_QUEEN, (self.x - SMALL_QUEEN_WIDTH // 2, self.y - SMALL_QUEEN_HEIGHT // 2))



